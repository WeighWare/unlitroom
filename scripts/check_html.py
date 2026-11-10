#!/usr/bin/env python3
"""Well-formedness check for the static HTML pages. Stdlib only.

The checker uses html.parser and requires:

- exactly one <!DOCTYPE html> before <html>
- exactly one <html>, <head>, and <body>, in that order
- <head> and <body> are direct children of <html>, and </head> precedes <body>
- every non-void element is closed in order
- no tags or non-whitespace text after </html>

Void elements (meta, link, img, and the rest of the HTML set) are not pushed
onto the stack. A trailing slash on a non-void tag is ignored, matching HTML.
"""

from __future__ import annotations

import sys
from html.parser import HTMLParser
from pathlib import Path

VOID_ELEMENTS = frozenset(
    {
        "area",
        "base",
        "br",
        "col",
        "embed",
        "hr",
        "img",
        "input",
        "link",
        "meta",
        "source",
        "track",
        "wbr",
    }
)

ROOT = Path(__file__).resolve().parent.parent
REQUIRED = ("html", "head", "body")


class WellFormedHTMLParser(HTMLParser):
    def __init__(self, filename: str) -> None:
        super().__init__(convert_charrefs=True)
        self.filename = filename
        self.errors: list[str] = []
        self.stack: list[tuple[str, int, int]] = []
        self.counts = {name: 0 for name in REQUIRED}
        self.doctype_count = 0
        self.doctype_seen = False
        self.saw_root = False
        self.head_closed = False
        self.finished_document = False
        self.fatal = False

    def error_at(
        self, message: str, line: int | None = None, col: int | None = None
    ) -> None:
        if line is None or col is None:
            line, offset = self.getpos()
            col = offset + 1
        self.errors.append(f"{self.filename}:{line}:{col}: {message}")

    def handle_decl(self, decl: str) -> None:
        if self.fatal:
            return
        line, offset = self.getpos()
        col = offset + 1
        self.doctype_seen = True
        if self.saw_root or self.stack:
            self.fatal = True
            self.error_at("doctype after the root element has started", line, col)
            return
        if decl.strip().lower() != "doctype html":
            self.fatal = True
            self.error_at(f"expected <!DOCTYPE html>, found <!{decl.strip()}>", line, col)
            return
        self.doctype_count += 1
        if self.doctype_count > 1:
            self.fatal = True
            self.error_at("duplicate doctype", line, col)

    def handle_data(self, data: str) -> None:
        if self.fatal or not data.strip():
            return
        if not self.saw_root:
            self.fatal = True
            self.error_at("non-whitespace content before <html>")
        elif self.finished_document:
            self.fatal = True
            self.error_at("non-whitespace content after </html>")

    def handle_starttag(self, tag: str, _attrs) -> None:
        self._open(tag)

    def handle_startendtag(self, tag: str, _attrs) -> None:
        # HTML ignores a trailing slash except as a void-element marker.
        self._open(tag)

    def _open(self, tag: str) -> None:
        if self.fatal:
            return
        line, offset = self.getpos()
        col = offset + 1
        if self.finished_document:
            self.fatal = True
            self.error_at(f"element <{tag}> after </html>", line, col)
            return
        if tag in self.counts:
            self.counts[tag] += 1
            if self.counts[tag] > 1:
                self.fatal = True
                self.error_at(f"duplicate <{tag}>", line, col)
                return
        if not self.saw_root:
            if tag != "html":
                self.fatal = True
                self.error_at(f"root element is <{tag}>, expected <html>", line, col)
                return
            self.saw_root = True
        if tag == "head":
            if not self.stack or self.stack[-1][0] != "html":
                self.fatal = True
                self.error_at("<head> must be a direct child of <html>", line, col)
                return
        elif tag == "body":
            if not self.stack or self.stack[-1][0] != "html":
                self.fatal = True
                self.error_at("<body> must be a direct child of <html>", line, col)
                return
            if not self.head_closed:
                self.fatal = True
                self.error_at("<body> starts before </head>", line, col)
                return
        if tag in VOID_ELEMENTS:
            return
        self.stack.append((tag, line, col))

    def handle_endtag(self, tag: str) -> None:
        if self.fatal:
            return
        line, offset = self.getpos()
        col = offset + 1
        if tag in VOID_ELEMENTS:
            self.fatal = True
            self.error_at(f"void element <{tag}> must not have an end tag", line, col)
            return
        if not self.stack:
            self.fatal = True
            self.error_at(f"unexpected </{tag}>", line, col)
            return
        open_tag, open_line, open_col = self.stack[-1]
        if open_tag != tag:
            self.fatal = True
            self.error_at(
                f"</{tag}> closes <{open_tag}> opened at {open_line}:{open_col}",
                line,
                col,
            )
            return
        self.stack.pop()
        if tag == "head":
            self.head_closed = True
        elif tag == "html":
            if self.stack:
                self.fatal = True
                self.error_at("</html> closed with elements still open", line, col)
                return
            self.finished_document = True

    def finish(self) -> None:
        super().close()
        if not self.doctype_seen:
            self.error_at("missing <!DOCTYPE html>", 1, 1)
        elif self.doctype_count != 1 and not any(
            "doctype" in error for error in self.errors
        ):
            self.error_at("document must contain exactly one <!DOCTYPE html>", 1, 1)
        # A fatal error stops the walk, so later unclosed-tag notes would
        # describe tags we deliberately did not keep parsing.
        if self.fatal:
            return
        for name in REQUIRED:
            if self.counts[name] == 0:
                self.error_at(f"missing <{name}>", 1, 1)
        for tag, line, col in self.stack:
            self.error_at(f"unclosed <{tag}>", line, col)


def check_file(path: Path) -> list[str]:
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError as exc:
        return [f"{path.name}:1:1: not valid UTF-8 ({exc})"]
    parser = WellFormedHTMLParser(path.name)
    try:
        parser.feed(text)
        parser.finish()
    except Exception as exc:
        return [f"{path.name}:1:1: html.parser failed ({exc})"]
    return parser.errors


def main(argv: list[str]) -> int:
    if argv:
        files = [Path(arg) for arg in argv]
    else:
        files = sorted(ROOT.glob("*.html"))
    if not files:
        print("no HTML files to check", file=sys.stderr)
        return 1
    missing = [path for path in files if not path.is_file()]
    if missing:
        for path in missing:
            print(f"{path}: not a file", file=sys.stderr)
        return 1
    errors: list[str] = []
    for path in files:
        errors.extend(check_file(path))
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"well-formed: {len(files)} file(s)")
    for path in files:
        print(f"  {path.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

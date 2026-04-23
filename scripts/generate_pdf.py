"""Generate styled PDF from markdown chapter files.

Usage:
    python scripts/generate_pdf.py <input.md> [<input2.md> ...] -o <output.pdf>
    python scripts/generate_pdf.py --sample      # generate Ch1 sample
"""

import argparse
import re
import sys
from pathlib import Path

import markdown
from weasyprint import HTML, CSS


PROJECT_ROOT = Path(__file__).resolve().parent.parent
STYLE_CSS = PROJECT_ROOT / "scripts" / "style.css"
FINAL_DIR = PROJECT_ROOT / "final"
COVER_IMAGE = PROJECT_ROOT / "assets" / "book-cover.png"


CHAPTER_NUMERALS = {
    "1": "01", "2": "02", "3": "03", "4": "04", "5": "05",
    "6": "06", "7": "07", "8": "08", "9": "09",
    "10": "10", "11": "11", "12": "12", "13": "13",
    "14": "14", "15": "15", "16": "16",
}


def render_chapter_title_page(ch_num: str, ch_title: str) -> str:
    """Render a full-bleed chapter title page using CSS class."""
    roman = CHAPTER_NUMERALS.get(ch_num, ch_num)
    return f"""
<section class="chapter-title-page">
    <div class="chapter-label">CHAPTER</div>
    <div class="flask-icon">⚗</div>
    <div class="chapter-number">{roman}</div>
    <div class="chapter-title">{ch_title}</div>
</section>
"""


def extract_chapter_header(md_text: str) -> tuple[str, str, str]:
    """From the leading '# บทที่ X\\n## Title\\n---\\n' block, extract (num, title, remainder)."""
    lines = md_text.lstrip().split("\n")

    ch_num = ""
    ch_title = ""
    remainder_start = 0

    # Line 1: # บทที่ N
    if lines and lines[0].startswith("# "):
        m = re.search(r"บทที่\s+(\d+)", lines[0])
        if m:
            ch_num = m.group(1)
        remainder_start = 1

    # Line 2: ## Title
    while remainder_start < len(lines) and lines[remainder_start].strip() == "":
        remainder_start += 1
    if remainder_start < len(lines) and lines[remainder_start].startswith("## "):
        ch_title = lines[remainder_start][3:].strip()
        remainder_start += 1

    # Skip trailing separator --- after title
    while remainder_start < len(lines) and (
        lines[remainder_start].strip() == "" or lines[remainder_start].strip() == "---"
    ):
        remainder_start += 1

    remainder = "\n".join(lines[remainder_start:])
    return ch_num, ch_title, remainder


def markdown_to_html_body(md_text: str) -> str:
    """Convert markdown body (without chapter header) to HTML."""
    html_body = markdown.markdown(
        md_text,
        extensions=["extra", "sane_lists", "tables", "nl2br"],
    )
    return html_body


def render_book_cover() -> str:
    """Render book cover as first full-bleed page."""
    if not COVER_IMAGE.exists():
        return ""
    return f"""
<section class="book-cover-page">
    <img src="file://{COVER_IMAGE}" alt="AI Money Mastery">
</section>
"""


def build_html_document(chapters: list[tuple[str, str, str]], include_cover: bool = True) -> str:
    """Build full HTML document.

    chapters is a list of (ch_num, ch_title, html_body).
    """
    pieces = []
    if include_cover:
        pieces.append(render_book_cover())
    for ch_num, ch_title, html_body in chapters:
        pieces.append(render_chapter_title_page(ch_num, ch_title))
        pieces.append(f'<article class="chapter-content">{html_body}</article>')
    pieces.append(
        '<div class="brand-footer">AI MONEY LAB</div>'
    )

    doc_body = "\n".join(pieces)

    return f"""<!DOCTYPE html>
<html lang="th">
<head>
    <meta charset="UTF-8">
    <title>AI Money Mastery</title>
</head>
<body>
{doc_body}
</body>
</html>
"""


def generate_pdf(input_paths: list[Path], output_path: Path) -> None:
    chapters = []
    for p in input_paths:
        md_text = p.read_text(encoding="utf-8")
        ch_num, ch_title, remainder = extract_chapter_header(md_text)
        html_body = markdown_to_html_body(remainder)
        chapters.append((ch_num, ch_title, html_body))
        print(f"  Processed: บทที่ {ch_num} — {ch_title}")

    html_doc = build_html_document(chapters)

    css = CSS(filename=str(STYLE_CSS))
    HTML(string=html_doc, base_url=str(PROJECT_ROOT)).write_pdf(
        str(output_path),
        stylesheets=[css],
    )

    size_kb = output_path.stat().st_size / 1024
    print(f"\n  PDF saved: {output_path}")
    print(f"  Size: {size_kb:.1f} KB")


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate styled PDF from markdown chapters")
    parser.add_argument("inputs", nargs="*", help="Markdown files")
    parser.add_argument("-o", "--output", help="Output PDF path")
    parser.add_argument(
        "--sample",
        action="store_true",
        help="Generate sample PDF using Ch1",
    )
    args = parser.parse_args()

    if args.sample:
        ch1 = PROJECT_ROOT / "manuscript" / "part-1" / "ch01-ai-is-not-tech.md"
        output = FINAL_DIR / "sample-ch01.pdf"
        print(f"Generating sample from {ch1.name}...")
        FINAL_DIR.mkdir(exist_ok=True)
        generate_pdf([ch1], output)
        return

    if not args.inputs or not args.output:
        parser.error("Provide input markdown files and -o output, or use --sample")

    input_paths = [Path(p) for p in args.inputs]
    output = Path(args.output)
    FINAL_DIR.mkdir(exist_ok=True)
    generate_pdf(input_paths, output)


if __name__ == "__main__":
    main()

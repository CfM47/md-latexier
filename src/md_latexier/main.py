import argparse
import os
from md_latexier.converter import md_to_latex
from templates.default import LATEX_TEMPLATE

VERSION = "0.1.0"

def main():
    parser = argparse.ArgumentParser(
        prog="md-latexier",
        description="Convert Markdown (.md) files into LaTeX (.tex) documents."
    )

    parser.add_argument(
        "input",
        help="Path to the Markdown file to convert."
    )

    parser.add_argument(
        "-o", "--output",
        help="Output .tex file path. If not provided, uses the same filename as input."
    )

    parser.add_argument(
        "-t", "--template",
        help="Choose a LaTeX template (currently only 'default' is available).",
        default="default"
    )

    parser.add_argument(
        "-v", "--version",
        action="version",
        version=f"md-latexier {VERSION}"
    )

    args = parser.parse_args()
    md_path = args.input

    # --- Validate input file ---
    if not os.path.exists(md_path):
        print(f"ERROR: File not found: {md_path}")
        exit(1)

    # --- Read Markdown content ---
    with open(md_path, "r", encoding="utf-8") as f:
        md_text = f.read()

    # --- Convert Markdown ---
    title, latex_content = md_to_latex(md_text)

    # --- Select template ---
    # TODO: add more templates
    template = LATEX_TEMPLATE  

    # --- Fill template ---
    final_tex = template.replace("TITLE_PLACEHOLDER", title)
    final_tex = final_tex.replace("CONTENT_PLACEHOLDER", latex_content)

    # --- Determine output path ---
    if args.output:
        tex_path = args.output
    else:
        tex_path = md_path.rsplit(".", 1)[0] + ".tex"

    # --- Write output file ---
    with open(tex_path, "w", encoding="utf-8") as f:
        f.write(final_tex)

    print("Converted successfully:")
    print(f" → {tex_path}")


if __name__ == "__main__":
    main()

import sys
import os
from md_latexier.converter import md_to_latex
from templates.default import LATEX_TEMPLATE

def main():
    if len(sys.argv) < 2:
        print("Uso: md-latexier archivo.md")
        sys.exit(1)

    md_path = sys.argv[1]

    if not os.path.exists(md_path):
        print("ERROR: No existe el archivo:", md_path)
        sys.exit(1)

    with open(md_path, "r", encoding="utf-8") as f:
        md_text = f.read()

    title, latex_content = md_to_latex(md_text)

    final_tex = LATEX_TEMPLATE.replace("TITLE_PLACEHOLDER", title)
    final_tex = final_tex.replace("CONTENT_PLACEHOLDER", latex_content)

    tex_path = md_path.replace(".md", ".tex")

    with open(tex_path, "w", encoding="utf-8") as f:
        f.write(final_tex)

    print("Convertido correctamente:")
    print(" →", tex_path)

if __name__ == "main":
    main()
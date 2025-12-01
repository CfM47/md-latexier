import re


def convert_inline_formatting(line):
    """Convierte bold, italics, code inline, links usando regex."""

    # **bold**
    line = re.sub(r"\*\*(.+?)\*\*", r"\\textbf{\1}", line)  # noqa: F821

    # *italic*
    line = re.sub(r"\*(.+?)\*", r"\\textit{\1}", line)

    # `inline code`
    line = re.sub(r"`([^`]+)`", r"\\texttt{\1}", line)

    # [texto](url)
    line = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r"\\href{\2}{\1}", line)

    return line


def md_to_latex(md_text):
    latex_lines = []
    title = "Document Title"

    inside_codeblock = False
    code_language = ""

    lines = md_text.split("\n")

    for line in lines:

        # -------------------------------
        #   Bloques de código
        # -------------------------------
        if line.startswith("```"):
            if not inside_codeblock:
                inside_codeblock = True
                code_language = line.replace("```", "").strip()
                if code_language == "":
                    code_language = "text"
                latex_lines.append(f"\\begin{{lstlisting}}[language={code_language}]")
            else:
                inside_codeblock = False
                latex_lines.append("\\end{lstlisting}")
            continue

        if inside_codeblock:
            latex_lines.append(line)
            continue

        # headings
        if line.startswith("# "):
            title = line[2:].strip()
            latex_lines.append(f"\\chapter{{{title}}}")
            continue

        elif line.startswith("## "):
            section_title = line[3:].strip()
            latex_lines.append(f"\\section{{{section_title}}}")
            continue

        elif line.startswith("### "):
            subsection_title = line[4:].strip()
            latex_lines.append(f"\\subsection{{{subsection_title}}}")
            continue

        elif line.startswith("#### "):
            sst = line[5:].strip()
            latex_lines.append(f"\\subsubsection{{{sst}}}")
            continue
        processed = convert_inline_formatting(line)
        latex_lines.append(processed)

    return title, "\n".join(latex_lines)
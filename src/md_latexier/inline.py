import re


def parse_inline_formatting(line):
    """Converts bold, italics, code inline, links using regex."""

    # **bold**
    line = re.sub(r"\*\*(.+?)\*\*", r"\\textbf{\1}", line)

    # *italic*
    line = re.sub(r"\*(.+?)\*", r"\\textit{\1}", line)

    # `inline code`
    line = re.sub(r"`([^`]+)`", r"\\texttt{\1}", line)

    # [texto](url)
    line = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r"\\href{\2}{\1}", line)

    return line

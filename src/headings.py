
def parse_heading(line: str) -> tuple[str, str] | None:
    """
    Converts markdown headers to latex, returns None if it is not a header
    
    returns (section_type, content) if it is a header, otherwise returns None
    """
    if line.startswith("# "):
        return "chapter", line[2:].strip()
    if line.startswith("## "):
        return "section", line[3:].strip()
    if line.startswith("### "):
        return "subsection", line[4:].strip()
    if line.startswith("#### "):
        return "subsubsection", line[5:].strip()

    return None
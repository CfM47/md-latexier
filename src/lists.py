from re import match, Match

from src.inline import parse_inline_formatting


def is_list_item(line: str):
    """Check if a line is a list item"""
    unordered = match(r"^(\s*)([-+*])\s+(.*)", line)
    ordered = match(r"^(\s*)(\d+)\.\s+(.*)", line)
    return unordered or ordered


def parse_list_item(match: Match[str], state):
    """Converts a list item to LaTeX."""
    # indent = len(match.group(1))

    # type identifier
    if match.group(2).isdigit():
        list_type = "enumerate"
        content = match.group(3)
    else:
        list_type = "itemize"
        content = match.group(3)

    # open list
    if not state["in_list"]:
        state["in_list"] = True
        state["list_type"] = list_type
        return f"\\begin{{{list_type}}}\n    \\item {parse_inline_formatting(content)}"

    # change list type
    if state["list_type"] != list_type:
        close = f"\\end{{{state['list_type']}}}"
        state["list_type"] = list_type
        return (
            close
            + "\n"
            + f"\\begin{{{list_type}}}\n    \\item {parse_inline_formatting(content)}"
        )

    # fallback item
    return f"    \\item {parse_inline_formatting(content)}"


def close_list(state):
    """Close list if open."""
    if state["in_list"]:
        state["in_list"] = False
        return f"\\end{{{state['list_type']}}}"
    return None
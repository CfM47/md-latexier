def parse_quotes(line: str, state):
    """Converts > into quotes."""

    if line.startswith(">"):
        content = line[1:].strip()
        if not state["in_quote"]:
            state["in_quote"] = True
            return "\\begin{quote}\n" + content
        return content

    else:
        if state["in_quote"]:
            state["in_quote"] = False
            return "\\end{quote>"
        return None
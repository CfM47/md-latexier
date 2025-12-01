from src.codeblocks import parse_codeblocks
from src.quotes import parse_quotes
from src.headings import parse_heading
from src.lists import close_list, is_list_item, parse_list_item
from src.inline import parse_inline_formatting


def md_to_latex(md_text):
    """
    Proccess each line converting them to latex
    """

    lines = md_text.split("\n")
    result = []

    state = {
        "in_code": False,
        "in_quote": False,
        "in_list": False,
        "list_type": None,
    }

    title = "Document Title"

    for line in lines:
        # 1) Codeblocks
        code_out = parse_codeblocks(line, state)
        if code_out is not None:
            result.append(code_out)
            continue

        if state["in_code"]:  # if in codeblock stop processing
            continue

        # 2) Blockquotes
        quote_out = parse_quotes(line, state)
        if quote_out is not None:
            result.append(quote_out)
            continue

        # 3) Lists
        match = is_list_item(line)
        if match:
            list_out = parse_list_item(match, state)
            result.append(list_out)
            continue
        else:
            close = close_list(state)
            if close:
                result.append(close)

        # 4) Headings
        heading = parse_heading(line)
        if heading:
            kind, text = heading
            result.append(f"\\{kind}{{{text}}}")
            if kind == "chapter":
                title = text
            continue

        # 5) Inline formatting
        line = parse_inline_formatting(line)
        result.append(line)

    # Close open structures
    if state["in_quote"]:
        result.append("\\end{quote}")
    close = close_list(state)
    if close:
        result.append(close)

    return title, "\n".join(result)
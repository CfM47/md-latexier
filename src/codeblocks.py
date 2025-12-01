def parse_codeblocks(line: str, state: dict):
    """Handles codeblocks (```lang)."""

    if line.strip().startswith("```"):
        lang = line.replace("```", "").strip()

        # Inicio del bloque
        if not state["in_code"]:
            state["in_code"] = True
            return f"\\begin{{lstlisting}}{"[language={lang}]" if lang else ""}"

        # Fin del bloque
        else:
            state["in_code"] = False
            return "\\end{lstlisting}"

    if state["in_code"]:
        return line  # No se procesa contenido dentro de bloques

    return None


def escape(input_string):

    escaped = input_string.translate(str.maketrans({
        "]":  r"\]",
        "[":  r"\[",
        "\\": r"\\",
        "^":  r"\^",
        "$":  r"\$",
        "*":  r"\*",
        ".":  r"\."}))
    return escaped

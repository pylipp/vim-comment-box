"""Module for creating boxes around text."""


def put_text_in_box(line, text_width, comment_char='#'):
    current_line_without_indent = line.strip()
    first_char_in_line = current_line_without_indent[0]
    first_char_col = line.find(first_char_in_line)
    indent = line[:first_char_col]
    text_line_length = text_width - first_char_col
    text_line_length_without_comment_chars = text_line_length -\
            2*len(comment_char)
    return [
        indent + text_line_length * comment_char,
        indent + comment_char + current_line_without_indent.center(
            text_line_length_without_comment_chars) + comment_char,
        indent + text_line_length * comment_char,
    ]

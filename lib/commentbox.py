"""Module for creating boxes around text."""


# TODO
# - filetype-specific boxes
# - format long lines


def create_box_elements(lines, text_width=80, comment_char=None):
    """Create modified text line and wrapping line acc. to given line, text
    width and comment character.
    """
    comment_char = comment_char or '#'
    first_line = lines[0]
    current_line_without_indent = first_line.strip()
    first_char_in_line = current_line_without_indent[0]
    first_char_col = first_line.find(first_char_in_line)
    indent = first_line[:first_char_col]
    text_line_length = text_width - first_char_col
    text_line_length_without_comment_chars = text_line_length -\
            2*len(comment_char)
    wrapping_line = indent + text_line_length * comment_char
    elements = [wrapping_line]
    for line in lines:
        elements.append(
            indent + comment_char + line.strip().center(
            text_line_length_without_comment_chars) + comment_char)
    return elements

def put_text_in_box(buffer, row, text_width, count=1, comment_char=None):
    """Put the text at line `row` in the `buffer` into a comment box."""
    elements = create_box_elements(
        # copy instead of slicing because TestBuffer doesn't support it
        [buffer[i-1] for i in range(row, row + count)],
        text_width=text_width, comment_char=comment_char)
    wrapping_line = elements[0]
    text_lines = elements[1:]
    for i, line in enumerate(text_lines):
        buffer[row + i - 1] = line
    buffer.append(wrapping_line, row - 1)
    buffer.append(wrapping_line, row + count)

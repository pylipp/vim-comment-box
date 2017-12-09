"""Module for creating boxes around text."""

from commentchar import get_comment_chars


def create_box_elements(lines, text_width=80, filetype=None):
    """Create modified text line and wrapping line acc. to given line, text
    width and filetype.
    """
    filetype = filetype or "python"
    comment_chars = get_comment_chars(filetype)

    first_line = lines[0]
    current_line_without_indent = first_line.strip()
    first_char_in_line = current_line_without_indent[0]
    first_char_col = first_line.find(first_char_in_line)
    indent = first_line[:first_char_col]

    text_line_length = text_width - first_char_col
    text_line_length_without_comment_chars = text_line_length -\
        comment_chars.size

    wrapping_line = indent + comment_chars.start +\
        text_line_length_without_comment_chars * comment_chars.fill +\
        comment_chars.end

    elements = [wrapping_line]
    for line in lines:
        elements.append(
            indent + comment_chars.start + line.strip().center(
            text_line_length_without_comment_chars) + comment_chars.end)

    return elements

def put_text_in_box(buffer, row, text_width, count=1, filetype=None):
    """Put the text at line `row` in the `buffer` into a comment box."""
    elements = create_box_elements(
        # copy instead of slicing because TestBuffer doesn't support it
        [buffer[i-1] for i in range(row, row + count)],
        text_width=text_width, filetype=filetype)

    for i, line in enumerate(elements[1:]):
        buffer[row + i - 1] = line

    wrapping_line = elements[0]
    buffer.append(wrapping_line, row - 1)
    buffer.append(wrapping_line, row + count)

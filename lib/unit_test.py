import unittest

from commentbox import create_box_elements, put_text_in_box


class TestCreateBoxElements(unittest.TestCase):

    def test_line_without_indent(self):
        lines = ["test line"]
        expected = [
            "#############",
            "# test line #",
        ]
        actual = create_box_elements(lines, text_width=13)
        self.assertListEqual(expected, actual)

    def test_line_with_indent(self):
        lines = ["    some code  "]
        expected = [
            "    ##############",
            "    # some code  #",
        ]
        actual = create_box_elements(lines, text_width=18)
        self.assertListEqual(expected, actual)


class TestBuffer(object):
    """Object that patches the behaviour of vim.buffer."""

    def __init__(self, *lines):
        self._lines = {i: l for i, l in enumerate(lines, 1)}

    def __getitem__(self, index):
        return self._lines[index]

    def __setitem__(self, index, item):
        self._lines[index] = item

    def append(self, line, row):
        if row in self._lines:
            row +=1
        self._lines[row] = line

    def __eq__(self, other):
        return repr(self) == repr(other)

    def __repr__(self):
        return '\n'.join((self._lines[k] for k in sorted(self._lines)))

class TestPutTextInBox(unittest.TestCase):

    def test_line_without_indent(self):
        buffer = TestBuffer("all men must die")
        put_text_in_box(buffer, 1, 20)
        expected = TestBuffer(
            "####################",
            "# all men must die #",
            "####################",
        )
        self.assertEqual(buffer, expected)

    def test_line_with_indent(self):
        buffer = TestBuffer("  class Foo")
        put_text_in_box(buffer, 1, 17, '-')
        expected = TestBuffer(
            "  ---------------",
            "  -  class Foo  -",
            "  ---------------",
        )
        self.assertEqual(buffer, expected)


if __name__ == "__main__":
    unittest.main()

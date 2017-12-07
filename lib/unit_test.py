import unittest

from commentbox import put_text_in_box


class TestPutTextInBox(unittest.TestCase):

    def test_line_without_indent(self):
        line = "test line"
        expected = [
            "#############",
            "# test line #",
            "#############",
        ]
        actual = put_text_in_box(line, 13)
        self.assertListEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()

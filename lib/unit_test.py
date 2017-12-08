import unittest

from commentbox import create_box_elements


class TestCreateBoxElements(unittest.TestCase):

    def test_line_without_indent(self):
        line = "test line"
        expected = [
            "#############",
            "# test line #",
            "#############",
        ]
        actual = create_box_elements(line, 13)
        self.assertListEqual(expected, actual)

    def test_line_with_indent(self):
        line = "    some code  "
        expected = [
            "    ##############",
            "    # some code  #",
            "    ##############",
        ]
        actual = create_box_elements(line, 18)
        self.assertListEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()

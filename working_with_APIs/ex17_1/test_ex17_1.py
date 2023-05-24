import unittest

import ex17_1 as ex17

class ExTestCases(unittest.TestCase):
    """Tests for ex17_1.py."""

    def setUp(self):
        self.raw_input = "JavaScript, RubY,C,Java,, , Go, c++, pythoN "
        self.formatted_langs = ['javascript', 'ruby', 'c', 'java', 'go', 
            'c++', 'python']

    def test_get_input_to_formatted(self):
        output = ex17.get_input_to_formatted(self.raw_input)
        self.assertEqual(output, self.formatted_langs)


if __name__ == '__main__':
    unittest.main()
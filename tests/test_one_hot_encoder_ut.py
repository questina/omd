import unittest

from one_hot_encoder import fit_transform

TEST_INPUT = ['I', 'love', 'cats', 'and', 'dogs', 'but', 'cats', 'more']
EXPECTED_OUTPUT = [
            ('I', [0, 0, 0, 0, 0, 0, 1]),
            ('love', [0, 0, 0, 0, 0, 1, 0]),
            ('cats', [0, 0, 0, 0, 1, 0, 0]),
            ('and', [0, 0, 0, 1, 0, 0, 0]),
            ('dogs', [0, 0, 1, 0, 0, 0, 0]),
            ('but', [0, 1, 0, 0, 0, 0, 0]),
            ('cats', [0, 0, 0, 0, 1, 0, 0]),
            ('more', [1, 0, 0, 0, 0, 0, 0]),
        ]


class TestOneHotEncoder(unittest.TestCase):
    def test_empty_input(self):
        actual = fit_transform([])
        expected = []
        self.assertEqual(actual, expected)

    def test_one_word(self):
        actual = fit_transform('avito')
        expected = [('avito', [1])]
        self.assertEqual(actual, expected)

    def test_multiple_words_as_list(self):
        self.assertListEqual(fit_transform(TEST_INPUT), EXPECTED_OUTPUT)

    def test_multiple_words_as_args(self):
        self.assertListEqual(fit_transform(*TEST_INPUT), EXPECTED_OUTPUT)

    def test_incorrect_input(self):
        self.assertRaises(TypeError, fit_transform, None)

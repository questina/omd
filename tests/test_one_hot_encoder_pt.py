import pytest

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


def test_empty_input():
    assert fit_transform([]) == []


def test_one_word():
    assert fit_transform('avito') == [('avito', [1])]


def test_multiple_words_as_list():
    assert fit_transform(TEST_INPUT) == EXPECTED_OUTPUT


def test_multiple_words_as_args():
    assert fit_transform(*TEST_INPUT) == EXPECTED_OUTPUT


def test_incorrect_input():
    with pytest.raises(TypeError):
        fit_transform()

from typing import Iterable, List, Optional

import pytest
from count_vectorizer import CountVectorizer

CORPUS = [
    'I love Cats and Dogs and cats equally',
    'I love cats more than dogs',
    'i have a dog, so i like dogs more',
]

CORPUS_DEFAULT_COUNT_MATRIX = [
    [1, 1, 2, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0],
    [2, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1],
]

# case without lowercase and with stop_words = {'dogs', 'more'}
CORPUS_COUNT_MATRIX_WITH_PARAMS = [
    [1, 1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 1, 1, 1, 1],
]


def test_default_constructor():
    vectorizer = CountVectorizer()
    assert vectorizer.lowercase is True
    assert len(vectorizer.stop_words) == 0


def test_constructor_with_params():
    vectorizer = CountVectorizer(lowercase=False, stop_words={'a', 'b'})
    assert vectorizer.lowercase is False
    assert vectorizer.stop_words == {'a', 'b'}


def test_default_fit_transform():
    vectorizer = CountVectorizer()
    matrix = vectorizer.fit_transform(CORPUS)
    assert len(matrix) == len(CORPUS_DEFAULT_COUNT_MATRIX)
    assert matrix[0] == CORPUS_DEFAULT_COUNT_MATRIX[0]
    assert matrix[1] == CORPUS_DEFAULT_COUNT_MATRIX[1]
    assert matrix[2] == CORPUS_DEFAULT_COUNT_MATRIX[2]


def test_fit_transform_with_params():
    vectorizer = CountVectorizer(lowercase=False, stop_words=['dogs', 'more'])
    matrix = vectorizer.fit_transform(CORPUS)
    assert len(matrix) == len(CORPUS_COUNT_MATRIX_WITH_PARAMS)
    assert matrix[0] == CORPUS_COUNT_MATRIX_WITH_PARAMS[0]
    assert matrix[1] == CORPUS_COUNT_MATRIX_WITH_PARAMS[1]
    assert matrix[2] == CORPUS_COUNT_MATRIX_WITH_PARAMS[2]


@pytest.mark.parametrize(
    'lowercase,stop_words,expected_feature_names',
    [
        (
                True,
                None,
                ['i', 'love', 'cats', 'and', 'dogs', 'equally',
                 'more', 'than', 'have', 'a', 'dog,', 'so', 'like']
        ),
        (
                False,
                None,
                ['I', 'love', 'Cats', 'and', 'Dogs', 'cats',
                 'equally', 'more', 'than', 'dogs', 'i', 'have',
                 'a', 'dog,', 'so', 'like'],
        ),
        (
                False,
                ['dogs', 'more'],
                ['I', 'love', 'Cats', 'and', 'Dogs', 'cats', 'equally',
                 'than', 'i', 'have', 'a', 'dog,', 'so', 'like']
        )
    ]
)
def test_get_feature_names(
        lowercase: bool,
        stop_words: Optional[Iterable[str]],
        expected_feature_names: List[str]
):
    vectorizer = CountVectorizer(lowercase=lowercase, stop_words=stop_words)
    with pytest.raises(Exception, match='Vocabulary not fitted yet'):
        vectorizer.get_feature_names()
    vectorizer.fit_transform(CORPUS)
    assert vectorizer.get_feature_names() == expected_feature_names

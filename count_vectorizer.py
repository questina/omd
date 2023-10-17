from typing import Iterable, List


class CountVectorizer:
    """
    Convert a collection of text documents to a document-term matrix.

    Parameters
    ------------
    lowercase: bool, default=True
        Cast all texts to lowercase before tokenizing.

    stop_words: Iterable[str], default=None
        Words that will be removed from text and won't be tokenized.

    Attributes
    ------------
    _words_to_idx: dict
        A mapping of terms to feature indices.
    """

    def __init__(
            self,
            lowercase: bool = True,
            stop_words: Iterable[str] = None
    ) -> None:
        if stop_words is None:
            stop_words = {}

        self._word_to_idx = None
        self.lowercase = lowercase
        self.stop_words = stop_words

    def _text_preprocessor(self, text: str) -> List[str]:
        """
        Process data input. Splits text into words.
        If attribute lowercase is True, converts text to lowercase.
        If attribute stop_words is not empty, removes stop words from text.

        :param text: input text for tokenization.
        :return: collection of words of processed text.
        """
        if self.lowercase:
            text = text.lower()
        preprocessed_text = [
            word for word in text.split() if word not in self.stop_words
        ]
        return preprocessed_text

    def fit_transform(self, corpus: Iterable[str]) -> List[int]:
        """
        Learn vocabulary of words and convert corpus to document-term matrix.

        :param corpus: collection of texts to tokenization.
        :return: processed texts in a form of document-term matrix.
        """
        self._word_to_idx = {}
        corpus_word_freq = []

        for text in corpus:
            text_word_freq = {}
            for word in self._text_preprocessor(text):
                self._word_to_idx[word] = self._word_to_idx.get(
                    word, len(self._word_to_idx)
                )
                word_idx = self._word_to_idx[word]
                text_word_freq[word_idx] = text_word_freq.get(word_idx, 0) + 1
            corpus_word_freq.append(text_word_freq)

        count_matrix = [
            [0 for _ in range(len(self._word_to_idx))]
            for _ in range(len(corpus))
        ]

        for i, text_word_freq in enumerate(corpus_word_freq):
            for word_idx in text_word_freq:
                count_matrix[i][word_idx] = text_word_freq[word_idx]

        return count_matrix

    def get_feature_names(self) -> List[str]:
        """
        Return tokens from vocabulary in order of their indices.
        If vocabulary was not fitted, raise error.

        :return: tokens from vocabulary.
        """
        if self._word_to_idx is None:
            raise Exception('Vocabulary not fitted yet')
        return [
            t for t, i in sorted(
                self._word_to_idx.items(),
                key=lambda dict_item: dict_item[1]
            )
        ]


if __name__ == '__main__':
    corpus = ['Crock Pot Pasta Never boil pasta again',
              'Pasta Pomodoro Fresh ingredients Parmesan to taste']
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())
    print(count_matrix)

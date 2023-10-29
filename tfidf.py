import math
from typing import List, Iterable

from count_vectorizer import CountVectorizer


class TfidfTransformer:
    """
    Transform a count matrix to a normalized tf-idf representation.
    """

    @staticmethod
    def _tf_transform(count_matrix: List[List[int]]) -> List[List[float]]:
        """
        Count tf (term frequency) vector for each document in count matrix.
        Term frequency is the measurement of how frequently
        a term occurs within a document.
        Its formula is as follows:
            tf = count of word in doc / num of words in doc

        :param count_matrix: matrix with count of each
        term in a form of document-term matrix.

        :return: matrix, containing tf scores,
        in a form of document-term matrix.
        """
        words_sums = [sum(count_vector) for count_vector in count_matrix]
        return [
            [word_cnt / words_num for word_cnt in count_vector]
            for count_vector, words_num in zip(count_matrix, words_sums)
        ]

    @staticmethod
    def _idf_transform(count_matrix: List[List[int]]) -> List[float]:
        """
        Count idf (inverse document frequency) vector for
        each document in count matrix.
        Inverse document frequency is a weight
        indicating how commonly a word is used.
        Its formula is as follows:
            idf = 1 + log(num of docs + 1 / num of docs containing term + 1)

        :param count_matrix: matrix with count of each
        term in a form of document-term matrix.

        :return: vector, containing idf score for each term.
        """
        documents_num = len(count_matrix)
        terms_num = len(count_matrix[0])
        words_cnt = [0] * terms_num

        for document in count_matrix:
            for i in range(terms_num):
                words_cnt[i] += 0 if document[i] == 0 else 1

        return [
            math.log((documents_num + 1) / (word_cnt + 1)) + 1
            for word_cnt in words_cnt
        ]

    def fit_transform(
        self,
        count_matrix: List[List[int]],
    ) -> List[List[float]]:
        """
        Count tf-idf score for each term in document-term matrix.
        Tf-idf is a common term weighting scheme in information retrieval.
        Its formula is as follows:
            tf-idf = tf * idf

        :param count_matrix: matrix with count of each
        term in a form of document-term matrix.

        :return: matrix, containing tf-idf scores,
        in a form of document-term matrix.
        """
        corpus_tf = self._tf_transform(count_matrix)
        corpus_idf = self._idf_transform(count_matrix)
        tfidf_score = []
        for doc_tf in corpus_tf:
            tfidf_score.append(
                [tf * idf for tf, idf in zip(doc_tf, corpus_idf)]
            )
        return tfidf_score


class TfidfVectorizer(CountVectorizer):
    """
    Convert a collection of raw documents to a matrix of TF-IDF features.

    Attributes
    ------------
        transformer: TfidfTransformer
        class object to transform documents count matrix
        to tf-idf representation.
    """

    def __init__(self):
        super().__init__()
        self.transformer = TfidfTransformer()

    def fit_transform(self, corpus: Iterable[str]) -> List[List[float]]:
        """
        Learn vocabulary and convert corpus to td-idf document-term matrix.
        :param corpus: collection of texts to tokenization.
        :return: processed texts in a form of tf-idf document-term matrix.
        """
        count_matrix = super().fit_transform(corpus)
        return self.transformer.fit_transform(count_matrix)


if __name__ == '__main__':
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste',
    ]
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())
    print(tfidf_matrix)

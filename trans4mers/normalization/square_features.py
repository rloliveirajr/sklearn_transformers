import numpy as np
from sklearn.base import TransformerMixin


class SquareFeatures(TransformerMixin):

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        return [[x_i ** 2 for x_i in x] for x in X]

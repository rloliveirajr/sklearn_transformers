import numpy as np
from sklearn.base import TransformerMixin


class StandardNormalization(TransformerMixin):

    def fit(self, X, y=None):
        pass

    def transform(self, X, y=None):
        normalization_func = lambda x: (x - x.mean()) / x.std()
        return list(map(normalization_func, X))

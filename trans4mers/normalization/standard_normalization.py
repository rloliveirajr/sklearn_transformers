import numpy as np
from sklearn.base import TransformerMixin


class StandardNormalization(TransformerMixin):

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        normalization_func = lambda x: ((x - np.mean(x)) / np.std(x))
        return list(map(normalization_func, X))

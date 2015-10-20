import numpy as np
from sklearn.base import TransformerMixin


class Log(TransformerMixin):

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        return [np.log(-x) for x in X]

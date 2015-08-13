import math
from sklearn.base import TransformerMixin


class Fingerprint(TransformerMixin):

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        return [self.trans_func_(x) for x in X]

    def trans_func_(self, x):
        return x
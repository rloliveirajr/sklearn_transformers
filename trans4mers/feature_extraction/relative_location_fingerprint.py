import numpy as np
from sklearn.base import TransformerMixin


class RelativeLocationFingerprint(TransformerMixin):

    def fit(self, X, y=None):
        pass

    def transform(self, X, y=None):
        return [self.hfl(x) for x in X]

    def hfl(self, row):
        values = row
        max_value = max(values)

        features = []
        for i in range(0, len(values)):
            for j in range(0, len(values)):
                if i == j:
                    continue
                r = values[i] / float(values[j])
                features.append(r)
        return features

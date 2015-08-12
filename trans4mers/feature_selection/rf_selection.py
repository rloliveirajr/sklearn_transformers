import numpy as np
from sklearn.base import TransformerMixin
from sklearn.ensemble import RandomForestClassifier


class RFSelection(TransformerMixin):

    def __init__(self, n_features=None, n_estimators=100):
        self.rf = RandomForestClassifier(n_estimators=n_estimators)
        self.n_features = None

        if n_features is not None:
            self.n_features = n_features

    def fit(self, X, y=None):
        self.rf.fit(X, y)

        importances = self.rf.feature_importances_
        ranking = np.argsort(importances)

        if self.n_features is None:
            self.n_features = round(X.shape[1]/2)

        self.threshold = importances[ranking[self.n_features]]
        return self

    def transform(self, X, y=None):
        return self.rf.transform(X, self.threshold)
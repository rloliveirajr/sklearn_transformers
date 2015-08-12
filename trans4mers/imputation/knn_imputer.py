import numpy as np
from functools import reduce
from sklearn.neighbors import KNeighborsRegressor
from sklearn.base import TransformerMixin


class KNNImputer(TransformerMixin):
    """
    Fill missing values using KNN Regressor
    """

    def __init__(self, k):
        self.k = k

    def fit(self, X, y=None):
        pass

    def transform(self, X, y=None):
        """
        :param X: multidimensional numpy array like.
        """
        rows, features = X.shape

        mask = list(map(lambda x: reduce(lambda h, t: h or t, x), np.isnan(X)))
        criteria_for_bad = np.where(mask)[0]
        criteria_for_good = np.where(mask == np.zeros(len(mask)))[0]

        X_bad = X[criteria_for_bad]
        X_good = X[criteria_for_good]

        knn = KNeighborsRegressor(n_neighbors=self.k)

        for idx, x_bad in zip(criteria_for_bad.tolist(), X_bad):
            missing = np.isnan(x_bad)
            bad_dim = np.where(missing)[0]
            good_dim = np.where(missing == False)[0]

            for d in bad_dim:
                x = X_good[:, good_dim]
                y = X_good[:, d]
                knn.fit(x, y)

                X[idx, d] = knn.predict(x_bad[good_dim])

        return X

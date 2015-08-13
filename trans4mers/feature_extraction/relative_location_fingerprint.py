import numpy as np
from .fingerprint import Fingerprint


class RelativeLocationFingerprint(Fingerprint):

    def trans_func_(self, row):
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

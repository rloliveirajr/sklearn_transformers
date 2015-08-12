from sklearn.base import TransformerMixin


class HyperbolicLocationFingerprint(TransformerMixin):

    def fit(self, X, y=None):
        pass

    def transform(self, X, y=None):
        return [self.hfl(x) for x in X]

    def hfl(self, row):
        '''
        M. Kjaergaard and C. Munk, "Hyperbolic Location Fingerprint:
        A calibration-free solution for handling differences in signal
        strength", in PerCom, pp. 110-116, 2008
        '''
        values = row
        max_value = max(values)

        features = []
        for i in range(0, len(values)):
            for j in range(0, len(values)):
                if i == j:
                    continue
                r = values[i] / float(values[j])
                a = 1.0 / -max_value
                normalization = math.log(a)
                nlr = math.log(r) - normalization
                features.append(nlr)
        return features

import math
from .fingerprint import Fingerprint


class Diff(Fingerprint):

    def trans_func_(self, row):
        '''
        F. Dong, Y. Chen, J. Liu, Q. Ning, and S. Piao, "A Calibration-free
        localiztion solution for handling signal strength variance", in
        MELT (Berlin, Heidelberg), pp. 79-90, Springer-Verlag, 2009
        '''
        values = row

        features = []
        for i in range(0, len(values)):
            for j in range(0, len(values)):
                if i == j:
                    continue
                r = values[i] - values[j]
                features.append(r)
        return features

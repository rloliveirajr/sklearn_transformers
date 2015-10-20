from .fingerprint import Fingerprint


class SSD(Fingerprint):

    def trans_func_(self, row):
        '''
        A. Mahtab Hossain, H. N. Van, Y. Jin, and W.-S. Soh, "Indoor
        Localization using multiple wireless technologies", in IEEE
        International Conference on Mobile Adhoc and Sensor Systems,
        pp. 1-8, 2007
        '''
        values = row
        row_1 = values[:-1]
        row_2 = values[1:]
        features = []
        for pair_i in zip(row_1, row_2):
            f = pair_i[0] - pair_i[1]
            features.append(f)
        return features

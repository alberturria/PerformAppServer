class MeansEntity(object):
    def __init__(self, arithmetic_mean, harmonic_mean, geometric_mean, trimmed_mean):
        self._arithmetic_mean = arithmetic_mean
        self._harmonic_mean = harmonic_mean
        self._geometric_mean = geometric_mean
        self._trimmed_mean = trimmed_mean

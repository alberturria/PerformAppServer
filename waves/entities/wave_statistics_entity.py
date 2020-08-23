class WaveStatisticsEntity(object):
    def __init__(self, id, kurtosis, entropy, maximum, minimum, zero_crossing_counts, arithmetic_mean, harmonic_mean,
                 geometric_mean, trimmed_mean, median, mode, variance):
        self._id = id
        self.kurtosis = kurtosis
        self.entropy = entropy
        self.maximum = maximum
        self.minimum = minimum
        self.zero_crossing_counts = zero_crossing_counts
        self.arithmetic_mean = arithmetic_mean
        self.harmonic_mean = harmonic_mean
        self.geometric_mean = geometric_mean
        self.trimmed_mean = trimmed_mean
        self.median = median
        self.mode = mode
        self.variance = variance

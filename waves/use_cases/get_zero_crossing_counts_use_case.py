import numpy as np

from waves.interfaces.use_cases.get_zero_crossing_counts_use_case_interface import GetZeroCrossingCountsUseCaseInterface


class GetZeroCrossingCountsUseCase(GetZeroCrossingCountsUseCaseInterface):
    def __init__(self, wave):
        self._wave = wave
        self._zero_crossing_counts = None

    def run(self):
        wave_array = np.array(self._wave)
        self._zero_crossing_counts = ((wave_array[:-1] * wave_array[1:]) < 0).sum()

    def get_result(self):
        return self._zero_crossing_counts

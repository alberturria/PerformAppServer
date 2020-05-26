from scipy.signal import welch
import numpy as np
from waves.interfaces.use_cases.get_psdf_use_case_interface import GetPSDFUseCaseInterface
from waves.use_cases.butter_filter_signal_use_case import ButterFilterUseCase


class GetPSDFUseCase(GetPSDFUseCaseInterface):
    def __init__(self, raw):
        self._raw = raw
        self._frequencies = None
        self._psdf = None

    def run(self):
        butter_filter_use_case = ButterFilterUseCase(self._raw)
        butter_filter_use_case.run()
        filtered = butter_filter_use_case.get_result()

        self._frequencies, self._psdf = welch(np.asarray(filtered), 1024, window="hamming", scaling="spectrum",
                                              nfft=len(filtered))

    def get_result(self):
        return self._frequencies, self._psdf

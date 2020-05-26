from statistics import mode

from scipy.stats import kurtosis
from waves.interfaces.use_cases.get_kurtosis_use_case_interface import GetKurtosisUseCaseInterface


class GetKurtosisUseCase(GetKurtosisUseCaseInterface):
    def __init__(self, wave):
        self._wave = wave
        self._kurtosis = None

    def run(self):
        self._kurtosis = kurtosis(self._wave)

    def get_result(self):
        return self._kurtosis

from statistics import variance

from waves.interfaces.use_cases.get_variance_use_case_interface import GetVarianceUseCaseInterface


class GetVarianceUseCase(GetVarianceUseCaseInterface):
    def __init__(self, wave):
        self._wave = wave
        self._variance = None

    def run(self):
        self._variance = variance(self._wave)

    def get_result(self):
        return self._variance

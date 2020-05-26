from statistics import median


from waves.interfaces.use_cases.get_median_use_case_interface import GetMedianUseCaseInterface


class GetMedianUseCase(GetMedianUseCaseInterface):
    def __init__(self, wave):
        self._wave = wave
        self._median = None

    def run(self):
        self._median = median(self._wave)

    def get_result(self):
        return self._median

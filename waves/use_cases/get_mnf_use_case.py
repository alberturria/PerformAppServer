from waves.interfaces.use_cases.get_mnf_use_case_interface import GetMNFUseCaseInterface
from waves.use_cases.get_psdf_use_case import GetPSDFUseCase


class GetMNFUseCase(GetMNFUseCaseInterface):
    def __init__(self, wave):
        self._wave = wave
        self.mnf = []
        self._window_size = 384
        self._increment = 192

    def run(self):
        number_of_windows = int((len(self._wave) - self._window_size) / self._increment) + 1
        start = 0
        end = self._window_size

        for window in range(number_of_windows):
            wave = self._wave[start:end]
            start = start + self._increment
            end = start + self._window_size

            window_mnf = self._calculate_mnf(wave)
            self.mnf.append(window_mnf)

    def get_result(self):
        return self.mnf

    def _calculate_mnf(self, wave):
        get_psdf_use_case = GetPSDFUseCase(wave)
        get_psdf_use_case.run()
        frequencies, psdf = get_psdf_use_case.get_result()
        numerator = 0
        denominator = 0

        for frequency_index in range(len(frequencies)):
            numerator = numerator + (psdf[frequency_index] * frequencies[frequency_index])
            denominator = denominator + psdf[frequency_index]

        return numerator / denominator

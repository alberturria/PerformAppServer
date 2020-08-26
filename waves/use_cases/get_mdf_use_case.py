from waves.interfaces.use_cases.get_mdf_use_case_interface import GetMDFUseCaseInterface
from waves.use_cases.butter_filter_signal_use_case import ButterFilterUseCase
from waves.use_cases.get_psdf_use_case import GetPSDFUseCase


class GetMDFUseCase(GetMDFUseCaseInterface):
    def __init__(self, wave):
        self._wave = wave
        self._mdf = []
        self._window_size = 384
        self._increment = 192

    def run(self):
        butter_use_case = ButterFilterUseCase(self._wave)
        butter_use_case.run()
        self._wave = butter_use_case.get_result()
        number_of_windows = int((len(self._wave) - self._window_size) / self._increment) + 1
        start = 0
        end = self._window_size

        for window in range(number_of_windows):
            wave = self._wave[start:end]
            start = start + self._increment
            end = start + self._window_size

            window_mnf = self._calculate_mdf(wave)
            self._mdf.append(window_mnf)

    def get_result(self):
        return self._mdf

    def _calculate_mdf(self, wave):
        get_psdf_use_case = GetPSDFUseCase(wave)
        get_psdf_use_case.run()
        frequencies, psdf = get_psdf_use_case.get_result()
        value = 0

        for frequency_index in range(len(frequencies)):
            value = value + psdf[frequency_index]

        return 1/2 * value

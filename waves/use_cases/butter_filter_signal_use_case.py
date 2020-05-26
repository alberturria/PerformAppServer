from scipy.signal import butter, filtfilt
from waves.interfaces.use_cases.butter_filter_use_case_interface import ButterFilterUseCaseInterface


class ButterFilterUseCase(ButterFilterUseCaseInterface):
    def __init__(self, wave):
        self._wave = wave
        self._filtered_wave = None

    def run(self):
        fs = 1024
        low_cut = 20
        high_cut = 450
        order = 5
        nyquist_frequency = 0.5 * int(fs)
        low = low_cut / nyquist_frequency
        high = high_cut / nyquist_frequency

        b, a = butter(order, [low, high], btype='band')
        self._filtered_wave = filtfilt(b, a, self._wave)

    def get_result(self):
        return self._filtered_wave

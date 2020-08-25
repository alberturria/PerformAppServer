import pywt
from scipy import signal

from waves.interfaces.use_cases.get_wavelet_use_case_interface import GetWaveletUseCaseInterface


class GetWaveletUseCase(GetWaveletUseCaseInterface):
    def __init__(self, wave):
        self._wave = wave
        self._power = None

    def run(self):
        coefficients = pywt.wavedec(self._wave, pywt.Wavelet('sym4'), level=9)
        f59, pj5 = signal.welch(coefficients[5], fs=1024)
        self._power = pj5.mean()

    def get_result(self):
        return self._power

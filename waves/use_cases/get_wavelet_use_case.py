import pywt
from scipy import signal

from waves.interfaces.use_cases.get_wavelet_use_case_interface import GetWaveletUseCaseInterface


class GetWaveletUseCase(GetWaveletUseCaseInterface):
    def __init__(self, wave):
        self._wave = wave
        self._power = None

    def run(self):
        ca5, cd4, cd5, cd3, cd2, cd1 = pywt.wavedec(self._wave, pywt.Wavelet('rbio3.1'), level=5)
        fa0, pj0 = signal.welch(ca5, fs=1024)
        f5, pj5 = signal.welch(cd5, fs=1024)
        f4, pj4 = signal.welch(cd4, fs=1024)
        f3, pj3 = signal.welch(cd3, fs=1024)
        f2, pj2 = signal.welch(cd2, fs=1024)
        f1, pj1 = signal.welch(cd1, fs=1024)

        final = pj0 + pj5 + pj4 + pj3 + pj2 + pj1
        self._power = final.mean()

    def get_result(self):
        return self._power

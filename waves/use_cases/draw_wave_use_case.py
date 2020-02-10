from waves.interfaces.use_cases.draw_wave_use_case_interface import DrawWaveUseCaseInterface
import matplotlib.pyplot as plt
import numpy as np


class DrawWaveUseCase(DrawWaveUseCaseInterface):
    def __init__(self, wave):
        self.wave = wave

    def run(self):
        xf = []
        for value in self.wave:
            xf.append(self.wave.index(value))

        plt.plot(xf, self.wave)
        plt.xlabel('Frequency')
        plt.ylabel('Amplitude')

        plt.title('MDF')

        plt.show()

    # def run(self):
    #
    #     n = len(self.wave)
    #     t = 1.0 / 800.0
    #     xf = np.linspace(0.0, 1.0 / (2.0 * t), int(n / 2))
    #
    #     plt.plot(xf, 2.0 / n * np.abs(self.wave[:n // 2]))
    #     plt.xlabel('Frequency')
    #     plt.ylabel('Amplitude')
    #
    #     plt.title('Wave')
    #
    #     plt.show()

from waves.interfaces.use_cases.get_peaks_and_valleys_use_case_interface import GetPeaksAndValleysUseCaseInterface
from scipy import signal
import numpy as np
import matplotlib.pyplot as plt

from waves.repositories.get_rms_data_access import GetRMSDataAccess


class GetPeaksAndValleysUseCase(GetPeaksAndValleysUseCaseInterface):
    def __init__(self, wave_id):
        self._wave_id = wave_id

    def run(self):
        get_rms_data_access = GetRMSDataAccess(self._wave_id)
        self._wave = get_rms_data_access.get_rms()
        peak_indexes = signal.argrelextrema(self._wave, np.greater)
        self._peak_indexes = peak_indexes[0]

        valley_indexes = signal.argrelextrema(self._wave, np.less)
        self._valley_indexes = valley_indexes[0]

###
        x_values = []
        for value in self._wave:
            x_values.append(self._wave.index(value))

        (fig, ax) = plt.subplots()
        ax.plot(x_values, self._wave)

        # Plot peaks.
        peak_x = peak_indexes
        peak_y = self._wave[peak_indexes]
        ax.plot(peak_x, peak_y, marker='o', linestyle='dashed', color='green', label="Peaks")

        # Plot valleys.
        valley_x = valley_indexes
        valley_y = self._wave[valley_indexes]
        ax.plot(valley_x, valley_y, marker='o', linestyle='dashed', color='red', label="Valleys")
###

    def get_peaks(self):
        return self._peak_indexes

    def get_valleys(self):
        return self._valley_indexes

    def get_peaks_and_valleys(self):
        pass

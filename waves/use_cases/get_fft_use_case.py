import numpy
from waves.interfaces.use_cases.get_fft_use_case_interface import GetFFTUseCaseInterface
from waves.repositories.get_raw_data_access import GetRAWDataAccess
from waves.repositories.get_rms_data_access import GetRMSDataAccess
import numpy as np



class GetFFTUSeCase(GetFFTUseCaseInterface):
    def __init__(self, wave_id):
        self.wave_id = wave_id
        self.fft = None

    def run(self):
        get_raw_data_access = GetRAWDataAccess(self.wave_id)
        rms = get_raw_data_access.get_raw()

        fft = numpy.fft.fft(rms)
        self.fft = fft.tolist()

        self.fft = np.abs(self.fft[:len(self.fft) // 2])

    def get_result(self):
        return self.fft

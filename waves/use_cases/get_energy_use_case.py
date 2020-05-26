from waves.interfaces.use_cases.get_energy_use_case_interface import GetEnergyUseCaseInterface
from waves.repositories.get_raw_data_access import GetRAWDataAccess
from scipy.fft import fft


class GetEnergyUseCase(GetEnergyUseCaseInterface):
    def __init__(self, wave_id):
        self._wave_id = wave_id
        self._energy = None

    def run(self):
        get_raw_data_access = GetRAWDataAccess(self._wave_id)
        raw = get_raw_data_access.get_raw()
        xf = fft(raw)
        self._energy = sum(abs(xf) ** 2) / len(xf)

    def get_result(self):
        return self._energy

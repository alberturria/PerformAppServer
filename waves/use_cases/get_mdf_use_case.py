from waves.interfaces.use_cases.get_mdf_use_case_interface import GetMDFUseCaseInterface


class GetMDFUseCase(GetMDFUseCaseInterface):
    def __init__(self, wave):
        self.wave = wave
        self.mdf = []

    def run(self):
        window = 1000
        for element_index in range(len(self.wave) - window):
            partial_wave = []
            for index in range(window):
                partial_wave.append(self.wave[element_index + index])

            self.mdf.append(self._partial_mdf(partial_wave))

    def get_result(self):
        return self.mdf

    def _partial_mdf(self, partial_wave, window=10):
        local_mdf = 0
        for power_spectrum in partial_wave:
            local_mdf = local_mdf + power_spectrum

        local_mdf = local_mdf / 2

        return local_mdf

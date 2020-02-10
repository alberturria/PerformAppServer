from waves.interfaces.use_cases.get_mnf_use_case_interface import GetMNFUseCaseInterface


class GetMNFUseCase(GetMNFUseCaseInterface):
    def __init__(self, wave):
        self.wave = wave
        self.mnf = []

    def run(self):
        window = 1000
        for element_index in range(len(self.wave) - window):
            partial_wave = {}
            for index in range(window):
                partial_wave[element_index + index] = (self.wave[element_index + index])

            self.mnf.append(self._partial_mnf(partial_wave))

    def get_result(self):
        return self.mnf

    def _partial_mnf(self, partial_wave, window=10):
        numerator = 0
        denominator = 0
        for key, value in partial_wave.items():
            numerator = numerator + key * value
            denominator = denominator + value

        local_mnf = numerator / denominator

        return local_mnf

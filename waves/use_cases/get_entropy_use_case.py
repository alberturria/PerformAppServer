from waves.interfaces.use_cases.get_entropy_use_case_interface import GetEntropyUseCaseInterface
from scipy.stats import entropy


class GetEntropyUseCase(GetEntropyUseCaseInterface):
    def __init__(self, wave):
        self._wave = wave
        self._entropy = None

    def run(self):
        self._entropy = entropy(self._wave)

    def get_result(self):
        return self._entropy

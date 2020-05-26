from statistics import mode

from waves.interfaces.use_cases.get_mode_use_case_interface import GetModeUseCaseInterface


class GetModeUseCase(GetModeUseCaseInterface):
    def __init__(self, wave):
        self._wave = wave
        self._mode = None

    def run(self):
        self._mode = mode(self._wave)

    def get_result(self):
        return self._mode

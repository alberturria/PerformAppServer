from waves.entities.value_position_entity import ValuePositionEntity

import pandas as pd
from waves.interfaces.use_cases.get_minimum_use_case_interface import GetMinimumUseCaseInterface


class GetMinimumUseCase(GetMinimumUseCaseInterface):
    def __init__(self, wave):
        self._wave = wave
        self._minimum = None
        self._minimum_position = None
        self._value_position_entity = None

    def run(self):
        df = pd.DataFrame(self._wave)
        self._minimum = df.min()[0]
        self._minimum_position = df.idxmin()[0]
        self._value_position_entity = ValuePositionEntity(self._minimum, self._minimum_position)

    def get_result(self):
        return self._value_position_entity

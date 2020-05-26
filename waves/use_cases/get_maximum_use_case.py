from waves.entities.value_position_entity import ValuePositionEntity
from waves.interfaces.use_cases.get_maximum_use_case_interface import GetMaximumUseCaseInterface

import pandas as pd


class GetMaximumUseCase(GetMaximumUseCaseInterface):
    def __init__(self, wave):
        self._wave = wave
        self._maximum = None
        self._maximum_position = None
        self._value_position_entity = None

    def run(self):
        df = pd.DataFrame(self._wave)
        self._maximum = df.max()[0]
        self._maximum_position = df.idxmax()[0]
        self._value_position_entity = ValuePositionEntity(self._maximum, self._maximum_position)

    def get_result(self):
        return self._value_position_entity

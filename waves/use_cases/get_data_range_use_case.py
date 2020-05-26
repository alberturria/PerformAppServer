from statistics import mode
import pandas as pd
from waves.interfaces.use_cases.get_data_range_use_case_interface import GetDataRangeUseCaseInterface


class GetDataRangeUseCase(GetDataRangeUseCaseInterface):
    def __init__(self, wave):
        self._wave = wave
        self._range = None

    def run(self):
        df = pd.DataFrame(self._wave)
        max = df.max()[0]
        min = df.min()[0]
        self._range = max - min

    def get_result(self):
        return self._range

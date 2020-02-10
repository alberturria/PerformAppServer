import ast
import math
import numpy as np

from waves.interfaces.repositories.get_raw_data_access_interface import GetRAWDataAccessInterface
from waves.models import Wave


class GetRAWDataAccess(GetRAWDataAccessInterface):
    def __init__(self, wave_id):
        self.wave_id = wave_id

    def get_raw(self):
        raw_with_nan = Wave.objects.get(id=self.wave_id).raw
        raw = raw_with_nan.replace('nan', "'0,0'")

        raw_list = ast.literal_eval(raw)
        result = []
        for value in raw_list:
            replaced_value = value.replace(',', '.')
            result.append(float(replaced_value))

        return result

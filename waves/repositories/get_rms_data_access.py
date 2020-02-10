import ast
from waves.interfaces.repositories.get_rms_data_access_interface import GetRMSDataAccessInterface
from waves.models import Wave


class GetRMSDataAccess(GetRMSDataAccessInterface):
    def __init__(self, wave_id):
        self.wave_id = wave_id

    def get_rms(self):
        rms = Wave.objects.get(id=self.wave_id).rms
        rms_list = ast.literal_eval(rms)
        result = []
        for value in rms_list:
            replaced_value = value.replace(',', '.')
            result.append(float(replaced_value))

        return result

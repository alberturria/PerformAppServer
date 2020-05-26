from waves.entities.wave_entity import WaveEntity
from waves.interfaces.repositories.get_wave_data_access_interface import GetWaveDataAccessInterface
from waves.models import Wave
from waves.repositories.get_raw_data_access import GetRAWDataAccess
from waves.repositories.get_rms_data_access import GetRMSDataAccess


class GetWaveDataAccess(GetWaveDataAccessInterface):

    def __init__(self, wave_id):
        self.wave_id = wave_id

    def get_wave(self):
        rms_data_access = GetRMSDataAccess(self.wave_id)

        rms = rms_data_access.get_rms()

        muscle = Wave.objects.get(id=self.wave_id).muscle
        raw_data_access = GetRAWDataAccess(self.wave_id)

        raw = raw_data_access.get_raw()
        avg_rms = Wave.objects.get(id=self.wave_id).avg_rms
        mvc = Wave.objects.get(id=self.wave_id).mvc
        historic_mvc = Wave.objects.get(id=self.wave_id).historic_mvc

        return WaveEntity(id=self.wave_id, muscle=muscle, rms=rms, raw=raw, avg_rms=avg_rms, mvc=mvc,
                          historic_mvc=historic_mvc)

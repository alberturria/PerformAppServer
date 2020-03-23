from waves.entities.wave_entity import WaveEntity
from waves.interfaces.repositories.get_waves_data_access_interface import GetWavesDataAccessInterface
from waves.models import Wave
from waves.repositories.get_raw_data_access import GetRAWDataAccess
from waves.repositories.get_rms_data_access import GetRMSDataAccess


class GetWavesDataAccess(GetWavesDataAccessInterface):

    def get_waves(self):
        waves = Wave.objects.all()
        waves_entities = []

        for wave in waves:
            retrieved_wave = self._get_wave(wave.id)
            waves_entities.append(retrieved_wave)
        return waves_entities

    def _get_wave(self, wave_id):
        rms_data_access = GetRMSDataAccess(wave_id)

        rms = rms_data_access.get_rms()

        muscle = Wave.objects.get(id=wave_id).muscle
        raw_data_access = GetRAWDataAccess(wave_id)

        raw = raw_data_access.get_raw()
        avg_rms = Wave.objects.get(id=wave_id).avg_rms
        mvc = Wave.objects.get(id=wave_id).mvc
        historic_mvc = Wave.objects.get(id=wave_id).historic_mvc

        return WaveEntity(id=wave_id, muscle=muscle, rms=rms, raw=raw, avg_rms=avg_rms, mvc=mvc,
                          historic_mvc=historic_mvc)

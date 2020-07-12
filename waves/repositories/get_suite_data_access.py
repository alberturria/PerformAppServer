import math

from waves.entities.suite_entity import SuiteEntity
from waves.entities.wave_entity import WaveEntity
from waves.interfaces.repositories.get_suite_data_access_interface import GetSuiteDataAccessInterface
from waves.models import Wave, Suite
from waves.repositories.get_raw_data_access import GetRAWDataAccess
from waves.repositories.get_rms_data_access import GetRMSDataAccess


class GetSuiteDataAccess(GetSuiteDataAccessInterface):

    def __init__(self, user_id, suite_id):
        self._user_id = user_id
        self._suite_id = suite_id

    def get_suite(self):
        suite = Suite.objects.get(id=self._suite_id, owner__id=self._user_id)
        suite_entity = SuiteEntity(suite.id, suite.name, suite.date, suite.owner.id, suite.owner.username)
        return suite_entity

    def get_waves(self):
        waves_id = Wave.objects.filter(suite__id=self._suite_id).values_list('id', flat=True)
        waves_entities = []
        for wave_id in waves_id:
            rms_data_access = GetRMSDataAccess(wave_id)
    
            rms = rms_data_access.get_rms()
    
            muscle = Wave.objects.get(id=wave_id).muscle
            raw_data_access = GetRAWDataAccess(wave_id)
    
            raw = raw_data_access.get_raw()
            multiplicator = math.floor((len(raw) / len(rms)))
            cutted_raw = []
            for index in range(0,len(rms)):
                cutted_raw.append(raw[index*multiplicator])

            avg_rms = Wave.objects.get(id=wave_id).avg_rms
            mvc = Wave.objects.get(id=wave_id).mvc
            historic_mvc = Wave.objects.get(id=wave_id).historic_mvc
    
            wave_entity = WaveEntity(id=wave_id, muscle=muscle, rms=rms, raw=cutted_raw, avg_rms=avg_rms, mvc=mvc,
                              historic_mvc=historic_mvc)
            waves_entities.append(wave_entity)

        return waves_entities

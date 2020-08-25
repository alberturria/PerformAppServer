from rest_framework.response import Response
from waves.entities.fatigue_entity import FatigueEntity
from waves.interfaces.use_cases.get_fatigue_analysis_use_case_interface import GetFatigueAnalysisUseCaseInterface
from waves.repositories.get_suite_data_access import GetSuiteDataAccess
from waves.use_cases.get_wavelet_use_case import GetWaveletUseCase


class GetFatigueAnalysisUseCase(GetFatigueAnalysisUseCaseInterface):
    def __init__(self, user_id, suite_id):
        self._suite_id = suite_id
        self._user_id = user_id

    def run(self):
        suite_data_access = GetSuiteDataAccess(user_id=self._user_id, suite_id=self._suite_id)
        waves_entities = suite_data_access.get_waves()
        result = []
        wavelet_use_case = GetWaveletUseCase(waves_entities[0]._raw)
        wavelet_use_case.run()
        muscle_1_power = wavelet_use_case.get_result()
        wavelet_use_case = GetWaveletUseCase(waves_entities[2]._raw)
        wavelet_use_case.run()
        muscle_2_power = wavelet_use_case.get_result()
        wavelet_use_case = GetWaveletUseCase(waves_entities[1]._raw)
        wavelet_use_case.run()
        muscle_3_power = wavelet_use_case.get_result()
        wavelet_use_case = GetWaveletUseCase(waves_entities[3]._raw)
        wavelet_use_case.run()
        muscle_4_power = wavelet_use_case.get_result()
        result.append(FatigueEntity(muscle_1_power=muscle_1_power, muscle_1_name=waves_entities[0]._muscle,
                                    muscle_2_power=muscle_2_power,
                                    muscle_2_name=waves_entities[2]._muscle))
        result.append(FatigueEntity(muscle_1_power=muscle_3_power, muscle_1_name=waves_entities[1]._muscle,
                                    muscle_2_power=muscle_4_power,
                                    muscle_2_name=waves_entities[3]._muscle))

        parsed_fatigue_entities = {}
        index = 0
        for fatigue_entity in result:
            parsed_fatigue_entities[index] = fatigue_entity.__dict__
            index += 1
        return Response(data=parsed_fatigue_entities, status=Response.status_code)

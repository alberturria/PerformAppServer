from waves.entities.fatigue_entity import FatigueEntity
from waves.interfaces.use_cases.fatigue_analysis_use_case_interface import FatigueAnalysisUseCaseInterface
from waves.use_cases.get_wavelet_use_case import GetWaveletUseCase


class FatigueAnalysisUseCase(FatigueAnalysisUseCaseInterface):
    def __init__(self, waves):
        self._waves = waves

    def run(self):
        result = []
        wavelet_use_case = GetWaveletUseCase(self._waves[0]._raw)
        wavelet_use_case.run()
        muscle_1_power = wavelet_use_case.get_result()
        wavelet_use_case = GetWaveletUseCase(self._waves[2]._raw)
        wavelet_use_case.run()
        muscle_2_power = wavelet_use_case.get_result()
        wavelet_use_case = GetWaveletUseCase(self._waves[1]._raw)
        wavelet_use_case.run()
        muscle_3_power = wavelet_use_case.get_result()
        wavelet_use_case = GetWaveletUseCase(self._waves[3]._raw)
        wavelet_use_case.run()
        muscle_4_power = wavelet_use_case.get_result()
        result.append(FatigueEntity(muscle_1_power=muscle_1_power, muscle_1_name=self._waves[0]._muscle,
                                    muscle_2_power=muscle_2_power,
                                    muscle_2_name=self._waves[2]._muscle))
        result.append(FatigueEntity(muscle_1_power=muscle_3_power, muscle_1_name=self._waves[1]._muscle,
                                    muscle_2_power=muscle_4_power,
                                    muscle_2_name=self._waves[3]._muscle))

        return result

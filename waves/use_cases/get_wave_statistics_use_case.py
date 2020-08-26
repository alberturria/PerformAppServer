from rest_framework.response import Response
from waves.entities.wave_statistics_entity import WaveStatisticsEntity
from waves.interfaces.use_cases.get_wave_statistics_use_case_interface import GetWaveStatisticsUseCaseInterface
from waves.repositories.get_suite_data_access import GetSuiteDataAccess
from waves.use_cases.get_energy_use_case import GetEnergyUseCase
from waves.use_cases.get_entropy_use_case import GetEntropyUseCase
from waves.use_cases.get_kurtosis_use_case import GetKurtosisUseCase
from waves.use_cases.get_maximum_use_case import GetMaximumUseCase
from waves.use_cases.get_mdf_use_case import GetMDFUseCase
from waves.use_cases.get_means_use_case import GetMeansUseCase
from waves.use_cases.get_median_use_case import GetMedianUseCase
from waves.use_cases.get_minimum_use_case import GetMinimumUseCase
from waves.use_cases.get_mnf_use_case import GetMNFUseCase
from waves.use_cases.get_mode_use_case import GetModeUseCase
from waves.use_cases.get_variance_use_case import GetVarianceUseCase
from waves.use_cases.get_zero_crossing_counts_use_case import GetZeroCrossingCountsUseCase


class GetWaveStatisticsUseCase(GetWaveStatisticsUseCaseInterface):
    def __init__(self, user_id, suite_id):
        self._user_id = user_id
        self._suite_id = suite_id

    def run(self):
        suite_data_access = GetSuiteDataAccess(self._user_id, self._suite_id)
        waves = suite_data_access.get_waves()
        self._parsed_waves_entities = {}
        self._statistics_entities = []
        index = 0

        for wave in waves:
            kurtosis_use_case = GetKurtosisUseCase(wave._rms)
            kurtosis_use_case.run()
            kurtosis = kurtosis_use_case.get_result()

            entropy_use_case = GetEntropyUseCase(wave._rms)
            entropy_use_case.run()
            entropy = entropy_use_case.get_result()

            maximum_use_case = GetMaximumUseCase(wave._rms)
            maximum_use_case.run()
            maximum = maximum_use_case.get_result()

            minimum_use_case = GetMinimumUseCase(wave._rms)
            minimum_use_case.run()
            minimum = minimum_use_case.get_result()

            zero_crossing_use_case = GetZeroCrossingCountsUseCase(wave._raw)
            zero_crossing_use_case.run()
            zero = zero_crossing_use_case.get_result()

            means_use_case = GetMeansUseCase(wave._rms)
            means_use_case.run()
            means = means_use_case.get_result()

            median_use_case = GetMedianUseCase(wave._rms)
            median_use_case.run()
            median = median_use_case.get_result()

            mode_use_case = GetModeUseCase(wave._rms)
            mode_use_case.run()
            mode = mode_use_case.get_result()

            variance_use_case = GetVarianceUseCase(wave._rms)
            variance_use_case.run()
            variance = variance_use_case.get_result()

            energy_use_case = GetEnergyUseCase(wave._raw)
            energy_use_case.run()
            energy = energy_use_case.get_result()

            mdf_use_case = GetMDFUseCase(wave._raw)
            mdf_use_case.run()
            mdf = mdf_use_case.get_result()

            mnf_use_case = GetMNFUseCase(wave._raw)
            mnf_use_case.run()
            mnf = mnf_use_case.get_result()

            wave_statistic_entity = WaveStatisticsEntity(wave._id, kurtosis, entropy, maximum._value, minimum._value, zero,
                                                         means._arithmetic_mean, means._harmonic_mean,
                                                         means._geometric_mean, means._trimmed_mean, median, mode,
                                                         variance, energy=energy, mdf=mdf, mnf=mnf)

            self._parsed_waves_entities[index] = wave_statistic_entity.__dict__
            self._statistics_entities.append(wave_statistic_entity)
            index += 1

    def get_entities(self):
        return self._statistics_entities

    def get_response(self):
        return Response(data=self._parsed_waves_entities, status=Response.status_code)

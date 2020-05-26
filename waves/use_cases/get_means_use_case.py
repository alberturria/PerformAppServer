from statistics import mean

from scipy.stats import hmean, gmean, tmean
from waves.entities.means_entity import MeansEntity
from waves.interfaces.use_cases.get_means_use_case_interface import GetMeansUseCaseInterface


class GetMeansUseCase(GetMeansUseCaseInterface):
    def __init__(self, wave):
        self._wave = wave
        self._arithmetic_mean = None
        self._harmonic_mean = None
        self._geometric_mean = None
        self._trimmed_mean = None
        self._means_entity = None

    def run(self):
        self._arithmetic_mean = mean(self._wave)
        self._harmonic_mean = hmean(self._wave)
        self._geometric_mean = gmean(self._wave)
        self._trimmed_mean = tmean(self._wave)
        self._means_entity = MeansEntity(self._arithmetic_mean, self._harmonic_mean, self._geometric_mean,
                                         self._trimmed_mean)

    def get_result(self):
        return self._means_entity

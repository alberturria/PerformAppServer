from waves.interfaces.use_cases.compare_all_rms_per_sections_use_case_interface import \
    CompareAllRMSPerSectionsUseCaseInterface
from waves.use_cases.get_sections_use_case import GetSectionsUseCase


class CompareAllRMSPerSectionsUseCase(CompareAllRMSPerSectionsUseCaseInterface):
    def __init__(self, waves):
        self._waves = waves
        self._values = []

    def run(self):
        for wave in self._waves:
            get_sections_use_case = GetSectionsUseCase(wave)
            get_sections_use_case.run()
            rms_sections = get_sections_use_case.get_rms_sections()
            for section in rms_sections:
                mean = section._values.mean()
                self._values.append([mean[0] / wave._mvc, wave._id])

    def get_result(self):
        return self._values

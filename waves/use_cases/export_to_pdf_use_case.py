from rest_framework.response import Response
from waves.adaptors.export_to_pdf_adaptor import ExportToPDFAdaptor
from waves.interfaces.use_cases.export_to_pdf_use_case_interface import ExportToPDFUseCaseInterface
from waves.repositories.get_diagnosis_data_access import GetDiagnosisDataAccess
from waves.repositories.get_patient_data_access import GetPatientDataAccess
from waves.repositories.get_suite_data_access import GetSuiteDataAccess
from waves.use_cases.get_wave_statistics_use_case import GetWaveStatisticsUseCase


class ExportToPDFUseCase(ExportToPDFUseCaseInterface):
    def __init__(self, user_id, suite_id, selected_options):
        self._user_id = user_id
        self._suite_id = suite_id
        self._selected_options = selected_options
        self.export_to_pdf_adaptor = None

    def run(self):
        suite_data_access = GetSuiteDataAccess(user_id=self._user_id, suite_id=self._suite_id)
        suite_entity = suite_data_access.get_suite()
        waves_entities = suite_data_access.get_waves()
        get_statistics_use_case = GetWaveStatisticsUseCase(self._user_id, self._suite_id)
        get_statistics_use_case.run()
        statistics_entities = get_statistics_use_case.get_entities()
        if suite_entity.patient_id:
            patient_data_access = GetPatientDataAccess(user_id=self._user_id, patient_id=suite_entity.patient_id)
            patient_entity = patient_data_access.get_patient()
        else:
            patient_entity = None

        if suite_entity.diagnosis_id:
            diagnosis_data_access = GetDiagnosisDataAccess(user_id=self._user_id,
                                                           diagnosis_id=suite_entity.diagnosis_id)
            diagnosis_entity = diagnosis_data_access.get_diagnosis()
        else:
            diagnosis_entity = None
        self.export_to_pdf_adaptor = ExportToPDFAdaptor(suite_entity, waves_entities, patient_entity, diagnosis_entity,
                                                        statistics_entities, self._selected_options)

    def get_pdf(self):
        return self.export_to_pdf_adaptor.get_pdf()

    def export(self):
        return self.export_to_pdf_adaptor.export()

from rest_framework.response import Response
from waves.adaptors.export_to_pdf_adaptor import ExportToPDFAdaptor
from waves.interfaces.use_cases.export_to_pdf_use_case_interface import ExportToPDFUseCaseInterface
from waves.repositories.get_suite_data_access import GetSuiteDataAccess


class ExportToPDFUseCase(ExportToPDFUseCaseInterface):
    def __init__(self, user_id, suite_id):
        self._user_id = user_id
        self._suite_id = suite_id

    def run(self):
        suite_data_access = GetSuiteDataAccess(user_id=self._user_id, suite_id=self._suite_id)
        suite_entity = suite_data_access.get_suite()
        waves_entities = suite_data_access.get_waves()
        export_to_pdf_adaptor = ExportToPDFAdaptor(suite_entity, waves_entities)
        return export_to_pdf_adaptor.export()

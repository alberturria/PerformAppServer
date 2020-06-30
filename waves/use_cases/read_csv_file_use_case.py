from rest_framework.response import Response
from waves.interfaces.use_cases.read_csv_file_use_case_interface import ReadCSVFileUseCaseInterface
from waves.repositories.read_csv_file_data_access import ReadCSVFileDataAccess


class ReadCSVFileUseCase(ReadCSVFileUseCaseInterface):
    def __init__(self, file, user_id):
        self._file = file
        self._user_id = user_id

    def run(self):
        read_csv_file_data_access = ReadCSVFileDataAccess(self._file, self._user_id)
        read_csv_file_data_access.import_data()
        return Response(data=self._user_id, status=Response.status_code)

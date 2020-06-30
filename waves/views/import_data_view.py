from rest_framework.response import Response
from rest_framework.views import APIView
from waves.use_cases.read_csv_file_use_case import ReadCSVFileUseCase


class ImportDataView(APIView):

    def post(self, request, user_id):
        try:
            file = request.FILES['file']
            read_imported_data_use_case = ReadCSVFileUseCase(file, user_id)
            read_imported_data_use_case.run()

        except Exception as exception:
            return Response(data='Error', status=500)

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from waves.use_cases.read_csv_file_use_case import ReadCSVFileUseCase


class ImportDataView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, user_id):
        try:
            if request.auth.user_id is not int(user_id):
                raise Exception
            file = request.FILES['file']
            read_imported_data_use_case = ReadCSVFileUseCase(file, user_id)
            read_imported_data_use_case.run()

        except Exception as exception:
            return Response(data='Error', status=500)

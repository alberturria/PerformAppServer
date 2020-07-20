from rest_framework.response import Response
from rest_framework.views import APIView
from waves.use_cases.create_sample_data_use_case import CreateSampleDataUseCase
from waves.use_cases.export_to_pdf_use_case import ExportToPDFUseCase


class ExportToPDFView(APIView):

    def post(self, request, user_id, suite_id):
        try:
            export_to_pdf_use_case = ExportToPDFUseCase(user_id, suite_id)
            return export_to_pdf_use_case.run()

        except Exception as exception:
            return Response(data='Error', status=403)

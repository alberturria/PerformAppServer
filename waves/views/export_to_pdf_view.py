from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from waves.entities.select_options_entity import SelectOptionsEntity
from waves.use_cases.export_to_pdf_use_case import ExportToPDFUseCase


class ExportToPDFView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, user_id, suite_id):
        try:
            if request.auth.user_id is not int(user_id):
                raise Exception
            selected_options = SelectOptionsEntity(request.data['patient'], request.data['diagnosis'],
                                                   request.data['muscles'])
            export_to_pdf_use_case = ExportToPDFUseCase(user_id, suite_id, selected_options)
            export_to_pdf_use_case.run()
            return export_to_pdf_use_case.export()

        except Exception as exception:
            return Response(data='Error', status=403)

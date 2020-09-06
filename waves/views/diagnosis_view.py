from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from waves.entities.diagnosis_entity import DiagnosisEntity
from waves.use_cases.delete_diagnosis_use_case import DeleteDiagnosisUseCase
from waves.use_cases.edit_diagnosis_use_case import EditDiagnosisUseCase
from waves.use_cases.get_diagnosis_use_case import GetDiagnosisUseCase


class DiagnosisView(APIView):
    permission_classes = (IsAuthenticated,)
    def delete(self, request, user_id, diagnosis_id):
        try:
            if request.auth.user_id is not int(user_id):
                raise Exception
            delete_diagnosis_use_case = DeleteDiagnosisUseCase(user_id, diagnosis_id)
            return delete_diagnosis_use_case.run()

        except Exception as exception:
            return Response(data='Error', status=500)

    def get(self, request, user_id, diagnosis_id):
        try:
            if request.auth.user_id is not int(user_id):
                raise Exception
            get_diagnosis_use_case = GetDiagnosisUseCase(user_id, diagnosis_id)
            return get_diagnosis_use_case.run()

        except Exception as exception:
            return Response(data='Error', status=500)

    def put(self, request, user_id, diagnosis_id):
        try:
            if request.auth.user_id is not int(user_id):
                raise Exception
            diagnosis_entity = self._create_diagnosis_entity(request.data)
            edit_diagnosis_use_case = EditDiagnosisUseCase(user_id, diagnosis_entity)
            return edit_diagnosis_use_case.run()

        except Exception as exception:
            return Response(data='Error', status=500)

    def _create_diagnosis_entity(self, data):
        id = data.get('id', None)
        name = data.get('name', None)
        description = data.get('description', None)
        video = data.get('video', None)
        suite_id = data.get('suiteId', None)
        owner_id = data.get('ownerId', None)

        diagnosis_entity = DiagnosisEntity(id, name, description, video,owner_id, suite_id)

        return diagnosis_entity
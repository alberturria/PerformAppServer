from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from waves.entities.diagnosis_entity import DiagnosisEntity
from waves.use_cases.create_diagnosis_use_case import CreateDiagnosisUseCase
from waves.use_cases.get_all_diagnoses_use_case import GetAllDiagnosesUseCase


class DiagnosesCatalogView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, user_id):
        try:
            if request.auth.user_id is not int(user_id):
                raise Exception
            get_all_diagnoses_use_case = GetAllDiagnosesUseCase(user_id)
            return get_all_diagnoses_use_case.run()

        except Exception as exception:
            return Response(data='Error', status=500)

    def post(self, request, user_id):
        try:
            if request.auth.user_id is not int(user_id):
                raise Exception
            diagnosis_entity = self._create_diagnosis_entity(request.data)
            create_diagnosis_use_case = CreateDiagnosisUseCase(user_id, diagnosis_entity)
            return create_diagnosis_use_case.run()

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

import json

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from waves.entities.custom_field_entity import CustomFieldEntity
from waves.entities.suite_entity import SuiteEntity
from waves.use_cases.create_suite_use_case import CreateSuiteUseCase
from waves.use_cases.get_all_suites_use_case import GetAllSuitesUseCase


class SuitesCatalogView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, user_id):
        try:
            if request.auth.user_id is not int(user_id):
                raise Exception
            get_all_sections_use_case = GetAllSuitesUseCase(user_id)
            return get_all_sections_use_case.run()

        except Exception as exception:
            return Response(data='Error', status=500)

    def post(self, request, user_id):
        try:
            if request.auth.user_id is not int(user_id):
                raise Exception
            suite_entity = self._create_suite_entity(request.data)
            create_suite_use_case = CreateSuiteUseCase(user_id, suite_entity)
            return create_suite_use_case.run()

        except Exception as exception:
            return Response(data='Error', status=500)

    def _create_suite_entity(self, data):
        id = data.get('id', None)
        name = data.get('name', None)
        date = data.get('date', None)
        user_id = data.get('userId', None)
        username = data.get('username', None)
        patient_id = data.get('patientId', None)
        diagnosis_id = data.get('diagnosisId', None)
        csv = data.get('csv', None)
        video = data.get('video', None)
        custom_fields = data.get('customFields', None)
        type = data.get('type', None)
        custom_fields_entities = []
        if custom_fields:
            custom_fields = json.loads(custom_fields)
            for custom_field in custom_fields:
                custom_field_entity = CustomFieldEntity(None, custom_field['parameter'], custom_field['value'], None)
                custom_fields_entities.append(custom_field_entity)

        suite_entity = SuiteEntity(id=id, name=name, date=date, user_id=user_id, username=username,
                                   patient_id=patient_id, diagnosis_id=diagnosis_id, csv=csv, video=video,
                                   custom_fields=custom_fields_entities, type=type)

        return suite_entity

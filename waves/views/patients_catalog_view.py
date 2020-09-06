from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from waves.entities.patient_entity import PatientEntity
from waves.use_cases.create_patient_use_case import CreatePatientUseCase
from waves.use_cases.get_all_patients_use_case import GetAllPatientsUseCase


class PatientsCatalogView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, user_id):
        try:
            if request.auth.user_id is not int(user_id):
                raise Exception
            get_all_patients_use_case = GetAllPatientsUseCase(user_id)
            return get_all_patients_use_case.run()

        except Exception as exception:
            return Response(data='Error', status=500)

    def post(self, request, user_id):
        try:
            if request.auth.user_id is not int(user_id):
                raise Exception
            patient_entity = self._create_patient_entity(request.data)
            create_patient_use_case = CreatePatientUseCase(user_id, patient_entity)
            return create_patient_use_case.run()

        except Exception as exception:
            return Response(data='Error', status=500)

    def _create_patient_entity(self, data):
        id = data.get('id', None)
        name = data.get('name', None)
        mail = data.get('mail', None)
        gender = data.get('gender', None)
        age = data.get('age', None)
        phone_number = data.get('phoneNumber', None)
        photo = data.get('photo', None)
        owner_id = data.get('ownerId', None)

        patient_entity = PatientEntity(id, name, mail, gender, age, phone_number, photo, owner_id)

        return patient_entity

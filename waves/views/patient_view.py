from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from waves.entities.patient_entity import PatientEntity
from waves.use_cases.delete_patient_use_case import DeletePatientUseCase
from waves.use_cases.edit_patient_use_case import EditPatientUseCase
from waves.use_cases.get_patient_use_case import GetPatientUseCase


class PatientView(APIView):
    permission_classes = (IsAuthenticated,)
    def delete(self, request, user_id, patient_id):
        try:
            if request.auth.user_id is not int(user_id):
                raise Exception
            delete_patient_use_case = DeletePatientUseCase(user_id, patient_id)
            return delete_patient_use_case.run()

        except Exception as exception:
            return Response(data='Error', status=500)

    def get(self, request, user_id, patient_id):
        try:
            get_patient_use_case = GetPatientUseCase(user_id, patient_id)
            return get_patient_use_case.run()

        except Exception as exception:
            return Response(data='Error', status=500)

    def put(self, request, user_id, patient_id):
        try:
            patient_entity = self._create_patient_entity(request.data)
            edit_patient_use_case = EditPatientUseCase(user_id, patient_entity)
            return edit_patient_use_case.run()

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

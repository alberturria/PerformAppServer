from django.contrib.auth.models import User
from waves.entities.patient_entity import PatientEntity
from waves.interfaces.repositories.create_sample_patients_data_access_interface import \
    CreateSamplePatientsDataAccessInterface
from waves.models import Patient


class CreateSamplePatientsDataAccess(CreateSamplePatientsDataAccessInterface):
    def __init__(self, user_id):
        self._user_id = user_id

    def create_sample_patients(self):
        owner = User.objects.get(id=self._user_id)
        patient1 = Patient(name='Rosa Figueroa', mail='albertoherrer+rosa@correo.ugr.es',
                           gender=2, age=23,
                           phone_number=635269945, owner=owner)
        patient2 = Patient(name='Manuel Díaz', mail='albertoherrer+manuel@correo.ugr.es',
                           gender=1, age=55,
                           phone_number=632759985, owner=owner)
        patient3 = Patient(name='Francisco Cabezas', mail='albertoherrer+francisco@correo.ugr.es',
                           gender=1, age=25,
                           phone_number=684966347, owner=owner)
        patient4 = Patient(name='Ana Heras', mail='albertoherrer+ana@correo.ugr.es',
                           gender=2, age=46,
                           phone_number=672351977, owner=owner)
        patient5 = Patient(name='Alberto Herrera', mail='albertoherrer@correo.ugr.es',
                           gender=1, age=22,
                           phone_number=678451659, owner=owner)
        patient1.save()
        patient2.save()
        patient3.save()
        patient4.save()
        patient5.save()

        patients = Patient.objects.filter(owner__id=self._user_id)
        result = []

        for patient in patients:
            patient_entity = PatientEntity(patient.id, patient.name, patient.mail, patient.gender, patient.age,
                                           patient.phone_number, patient.photo.url, patient.owner.id)
            result.append(patient_entity)

        return result

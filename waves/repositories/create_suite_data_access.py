from django.contrib.auth.models import User
from waves.interfaces.repositories.create_suite_data_access_interface import CreateSuiteDataAccessInterface
from waves.models import Suite, Patient, CustomField, Diagnosis
from waves.repositories.read_csv_file_data_access import ReadCSVFileDataAccess


class CreateSuiteDataAccess(CreateSuiteDataAccessInterface):
    def __init__(self, user_id, suite_entity):
        self._user_id = user_id
        self._suite_entity = suite_entity

    def create_suite(self):
        owner = User.objects.get(id=self._user_id)
        patient = None
        if self._suite_entity.patient_id:
            patient = Patient.objects.get(id=self._suite_entity.patient_id)

        suite = Suite(name=self._suite_entity.name, date=self._suite_entity.date, patient=patient,
                      owner=owner, video=self._suite_entity.video)

        suite.save()

        if self._suite_entity.diagnosis_id:
            diagnosis = Diagnosis.objects.get(id=self._suite_entity.diagnosis_id)
            diagnosis.suite = suite
            diagnosis.save()

        read_csv_data_access = ReadCSVFileDataAccess(self._suite_entity.csv, self._user_id, suite.id)
        read_csv_data_access.import_data()

        if self._suite_entity.custom_fields:
            for custom_field_entity in self._suite_entity.custom_fields:
                custom_field = CustomField(parameter=custom_field_entity.parameter, value=custom_field_entity.value,
                                           suite=suite)
                custom_field.save()

        return suite.id

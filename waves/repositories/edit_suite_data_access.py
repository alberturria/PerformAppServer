from django.contrib.auth.models import User
from waves.interfaces.repositories.edit_suite_data_access_interface import EditSuiteDataAccessInterface
from waves.models import Suite, Patient, Diagnosis, CustomField, Wave
from waves.repositories.read_csv_file_data_access import ReadCSVFileDataAccess


class EditSuiteDataAccess(EditSuiteDataAccessInterface):

    def __init__(self, user_id, suite_entity):
        self._user_id = user_id
        self._suite_entity = suite_entity

    def edit_suite(self):
        owner = User.objects.get(id=self._user_id)
        suite = Suite.objects.get(id=self._suite_entity.id)
        previous_diagnoses = Diagnosis.objects.filter(suite__id=suite.id)

        self._delete_previous_waves(suite)
        self._delete_previous_custom_fields(suite)

        if previous_diagnoses:
            for previous_diagnosis in previous_diagnoses:
                previous_diagnosis.suite = None
                previous_diagnosis.save()

        if self._suite_entity.patient_id:
            patient = Patient.objects.get(id=self._suite_entity.patient_id)
            suite.patient = patient

        if self._suite_entity.diagnosis_id:
            diagnosis = Diagnosis.objects.get(id=self._suite_entity.diagnosis_id)
            diagnosis.suite = suite
            diagnosis.save()

        suite.name = self._suite_entity.name
        suite.date = self._suite_entity.date
        suite.owner = owner
        suite.video = self._suite_entity.video
        suite.type = self._suite_entity.type

        suite.save()

        read_csv_data_access = ReadCSVFileDataAccess(self._suite_entity.csv, self._user_id, suite.id)
        read_csv_data_access.import_data()

        if self._suite_entity.custom_fields:
            for custom_field_entity in self._suite_entity.custom_fields:
                custom_field = CustomField(parameter=custom_field_entity.parameter, value=custom_field_entity.value,
                                           suite=suite)
                custom_field.save()

        return suite.id

    def _delete_previous_waves(self, suite):
        related_waves = Wave.objects.filter(suite_id=self._suite_entity.id)

        for wave in related_waves:
            wave.delete()

    def _delete_previous_custom_fields(self, suite):
        related_custom_fields = CustomField.objects.filter(suite_id=self._suite_entity.id)

        for custom_field in related_custom_fields:
            custom_field.delete()

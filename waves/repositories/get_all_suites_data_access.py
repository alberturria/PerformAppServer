from waves.entities.custom_field_entity import CustomFieldEntity
from waves.entities.suite_entity import SuiteEntity
from waves.interfaces.repositories.get_all_suites_data_access_interface import GetAllSuitesDataAccessInterface
from waves.models import Suite, Diagnosis, CustomField


class GetAllSuitesDataAccess(GetAllSuitesDataAccessInterface):
    def __init__(self, user_id):
        self._user_id = user_id

    def get_suites(self):
        suites = Suite.objects.filter(owner__id=self._user_id)
        result = []

        for suite in suites:
            possible_diagnosis = Diagnosis.objects.filter(suite__id=suite.id).first()
            diagnosis_id = possible_diagnosis.id if possible_diagnosis else None
            diagnosis_name = possible_diagnosis.name if possible_diagnosis else None
            patient_name = suite.patient.name if suite.patient else None

            custom_fields_entities = []
            custom_fields = CustomField.objects.filter(suite__id=suite.id)
            for custom_field in custom_fields:
                custom_fields_entities.append(
                    CustomFieldEntity(custom_field.id, custom_field.parameter, custom_field.value, suite.id).__dict__)

            suite_entity = SuiteEntity(id=suite.id, name=suite.name, date=suite.date, user_id=suite.owner.id,
                                       username=suite.owner.username, patient_id=suite.patient_id,
                                       patient_name=patient_name, diagnosis_id=diagnosis_id,
                                       diagnosis_name=diagnosis_name, csv=None, video=None,
                                       custom_fields=custom_fields_entities, type=suite.type)
            result.append(suite_entity)

        return result

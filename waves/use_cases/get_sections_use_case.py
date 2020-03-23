import pandas as pd
from waves.entities.section_entity import SectionEntity
from waves.interfaces.use_cases.get_sections_use_case_interface import GetSectionsUseCaseInterface


class GetSectionsUseCase(GetSectionsUseCaseInterface):
    def __init__(self, wave_entity):
        self._wave_entiy = wave_entity
        self._rms_values = None
        self._raw_values = None
        self._rms_indexes = []
        self._raw_indexes = []
        self._result = []
        self._rms_sections = []
        self._raw_sections = []

    def run(self):
        self._rms_values = pd.DataFrame(self._wave_entiy._rms)
        self._raw_values = pd.DataFrame(self._wave_entiy._raw)

        self._get_rms_sections()
        self._get_raw_sections()

    def get_rms_sections(self):
        return self._rms_sections

    def get_raw_sections(self):
        return self._raw_sections

    def _get_rms_sections(self):
        threshold = float(self._rms_values.max() * 0.1)
        in_section = False
        section = []

        for index, row in self._rms_values.iterrows():
            if row[0] > threshold and not in_section:
                section.append(index)
                in_section = True
            if row[0] < threshold and in_section:
                section.append(index)
                self._rms_indexes.append(section)
                section = []
                in_section = False
            index += 1

        self._create_rms_section_entities()

    def _get_raw_sections(self):
        threshold = float(self._raw_values.max() * 0.1)
        in_section = False
        section = []

        for index, row in self._raw_values.iterrows():
            if row[0] > threshold and not in_section:
                section.append(index)
                in_section = True
            if row[0] < threshold and in_section:
                section.append(index)
                self._raw_indexes.append(section)
                section = []
                in_section = False
            index += 1

        self._create_raw_section_entities()

    def _create_rms_section_entities(self):
        for section in self._rms_indexes:
            start = section[0]
            end = section[1]
            values = self._rms_values[start:end]
            section_entity = SectionEntity(start, end, values, self._wave_entiy._id)
            self._rms_sections.append(section_entity)

    def _create_raw_section_entities(self):
        for section in self._raw_indexes:
            start = section[0]
            end = section[1]
            values = self._raw_values[start:end]
            section_entity = SectionEntity(start, end, values, self._wave_entiy._id)
            self._raw_sections.append(section_entity)

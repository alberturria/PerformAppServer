import base64
import io
from io import BytesIO

import xhtml2pdf.pisa as pisa
from django.http import HttpResponse
from django.template.loader import get_template
import matplotlib.pyplot as plt

from waves.interfaces.adaptors.export_to_pdf_adaptor_interface import ExportToPDFAdaptorInterface


class ExportToPDFAdaptor(ExportToPDFAdaptorInterface):
    def __init__(self, suite_entity, waves_entities, patient_entity, diagnosis_entity, statistics_entities,
                 selected_options):
        self._suite_entity = suite_entity
        self._waves_entities = waves_entities
        self._patient_entity = patient_entity
        self._diagnosis_entity = diagnosis_entity
        self._selected_options = selected_options
        self._statistics_entities = statistics_entities
        self._info_dict = {}

    def export(self):
        self._handle_info()
        template = get_template('suite_to_pdf.html')
        html = template.render(self._info_dict)
        result = io.BytesIO()
        self._pdf = pisa.pisaDocument(io.BytesIO(html.encode("UTF-8")), result)

        if not self._pdf.err:
            return HttpResponse(result.getvalue(), content_type='application/pdf')
        return None

    def get_pdf(self):
        self._handle_info()
        template = get_template('suite_to_pdf.html')
        html = template.render(self._info_dict)
        result = io.BytesIO()
        self._pdf = pisa.pisaDocument(io.BytesIO(html.encode("UTF-8")), result)

        if not self._pdf.err:
            return result.getvalue()

    def _handle_info(self):
        self._info_dict['suite_name'] = self._suite_entity.name
        self._info_dict['suite_date'] = self._suite_entity.date
        self._info_dict['suite_owner'] = self._suite_entity.username
        self._info_dict['all_waves_figure'] = self._get_all_waves_figure()
        self._info_dict['waves'] = []
        self._info_dict['statistics'] = []

        for wave in self._waves_entities:
            self._add_wave_information(wave)

        self._add_patient_if_needed()
        self._add_diagnosis_if_needed()
        self._add_muscles_if_needed()

    def _add_wave_information(self, wave):
        wave_dict = {}
        wave_dict['muscle'] = wave._muscle
        wave_dict['mvc'] = wave._mvc
        wave_dict['historic_mvc'] = wave._historic_mvc

        wave_dict['rms_figure'] = self._get_rms_figure(wave)

        self._info_dict['waves'].append(wave_dict)

    def _get_rms_figure(self, wave):
        fig = plt.figure(figsize=(8, 5))
        plt.plot(wave._rms)
        plt.xlabel('Tiempo (0.25s)')
        plt.ylabel('Amplitud (µV)')

        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image_png = buffer.getvalue()
        buffer.close()

        graphic = base64.b64encode(image_png)
        return graphic.decode('utf-8')

    def _get_all_waves_figure(self):
        fig = plt.figure(figsize=(8, 4))
        for wave in self._waves_entities:
            plt.plot(wave._rms)
        plt.xlabel('Tiempo (0.25s)')
        plt.ylabel('Amplitud (µV)')

        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image_png = buffer.getvalue()
        buffer.close()

        graphic = base64.b64encode(image_png)
        return graphic.decode('utf-8')

    def _add_patient_if_needed(self):
        if self._selected_options.patient and self._patient_entity:
            self._info_dict['patient'] = True
            self._info_dict['patient_name'] = self._patient_entity.name
            self._info_dict['patient_mail'] = self._patient_entity.mail
            if self._patient_entity.gender == 1:
                self._info_dict['patient_gender'] = 'Masculino'
            elif self._patient_entity.gender == 2:
                self._info_dict['patient_gender'] = 'Femenino'
            else:
                self._info_dict['patient_gender'] = 'Otro'
            self._info_dict['patient_age'] = self._patient_entity.age
            self._info_dict['patient_phone'] = self._patient_entity.phone_number

        else:
            self._info_dict['patient'] = False

    def _add_diagnosis_if_needed(self):
        if self._selected_options.diagnosis and self._diagnosis_entity:
            self._info_dict['diagnosis'] = True
            self._info_dict['diagnosis_name'] = self._diagnosis_entity.name
            self._info_dict['diagnosis_description'] = self._diagnosis_entity.description
        else:
            self._info_dict['diagnosis'] = False

    def _add_muscles_if_needed(self):
        if self._selected_options.muscles and self._statistics_entities:
            self._info_dict['muscles'] = True
            for statistic in self._statistics_entities:
                statistic_dict = {}

                statistic_dict['kurtosis'] = statistic.kurtosis
                statistic_dict['entropy'] = statistic.entropy
                statistic_dict['maximum'] = statistic.maximum
                statistic_dict['minimum'] = statistic.minimum
                statistic_dict['zero_crossing_counts'] = statistic.zero_crossing_counts
                statistic_dict['arithmetic_mean'] = statistic.arithmetic_mean
                statistic_dict['harmonic_mean'] = statistic.harmonic_mean
                statistic_dict['geometric_mean'] = statistic.geometric_mean
                statistic_dict['trimmed_mean'] = statistic.trimmed_mean
                statistic_dict['median'] = statistic.median
                statistic_dict['mode'] = statistic.mode
                statistic_dict['variance'] = statistic.variance
                self._info_dict['statistics'].append(statistic_dict)

            self._info_dict['wave_with_statistics'] = zip(self._info_dict['waves'], self._info_dict['statistics'])

        else:
            self._info_dict['muscles'] = False

import base64
import io
from io import BytesIO

import xhtml2pdf.pisa as pisa
from django.http import HttpResponse
from django.template.loader import get_template
import matplotlib.pyplot as plt

from waves.interfaces.adaptors.export_to_pdf_adaptor_interface import ExportToPDFAdaptorInterface


class ExportToPDFAdaptor(ExportToPDFAdaptorInterface):
    def __init__(self, suite_entity, waves_entities):
        self._suite_entity = suite_entity
        self._waves_entities = waves_entities
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

    def _handle_info(self):
        self._info_dict['suite_name'] = self._suite_entity.name
        self._info_dict['suite_date'] = self._suite_entity.date
        self._info_dict['suite_owner'] = self._suite_entity.username
        self._info_dict['all_waves_figure'] = self._get_all_waves_figure()
        self._info_dict['waves'] = []

        for wave in self._waves_entities:
            self._add_wave_information(wave)

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

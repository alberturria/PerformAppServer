import os
from decouple import config

from postmarker.core import PostmarkClient
from waves.interfaces.use_cases.send_mail_use_case_interface import SendMailUseCaseInterface
from waves.repositories.get_patient_data_access import GetPatientDataAccess
from waves.repositories.get_suite_data_access import GetSuiteDataAccess
from waves.use_cases.export_to_pdf_use_case import ExportToPDFUseCase


class SendMailUseCase(SendMailUseCaseInterface):
    def __init__(self, user_id, suite_id, selected_options):
        self._user_id = user_id
        self._suite_id = suite_id
        self._selected_options = selected_options

    def run(self):
        export_to_pdf_use_case = ExportToPDFUseCase(self._user_id, self._suite_id, self._selected_options)
        export_to_pdf_use_case.run()
        pdf = export_to_pdf_use_case.get_pdf()
        suite_data_access = GetSuiteDataAccess(self._user_id, self._suite_id)
        suite = suite_data_access.get_suite()
        patient_data_access = GetPatientDataAccess(self._user_id, suite.patient_id)
        patient = patient_data_access.get_patient()

        postmark = PostmarkClient(os.getenv('POSTMARK_KEY', config('POSTMARK_KEY')))

        email = postmark.emails.Email(
            From='albertoherrer@correo.ugr.es',
            To=patient.mail,
            Subject='Notificación de PerformApp',
            HtmlBody='<html><body>Querido usuario de PerformApp, en este mensaje se adjunta la información relativa a su prueba. <br> Tenga un buen día. <br> El equipo de PerformApp.</body></html>'
        )

        email.attach_binary(content=pdf, filename='readme.pdf')

        # return email.send()

class SuiteEntity(object):
    def __init__(self, id, name, date, user_id, username, patient_id=None, diagnosis_id=None, csv=None, video=None,
                 custom_fields=None):
        self.id = id
        self.name = name
        self.date = date
        self.user_id = user_id
        self.username = username
        self.patient_id = patient_id
        self.diagnosis_id = diagnosis_id
        self.csv = csv
        self.video = video
        self.custom_fields = custom_fields

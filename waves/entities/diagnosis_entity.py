class DiagnosisEntity(object):
    def __init__(self, id, name, description, video, owner_id, suite_id):
        self.id = id
        self.name = name
        self.description = description
        self.video = video
        self.owner_id = owner_id
        self.suite_id = suite_id

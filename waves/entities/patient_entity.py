class PatientEntity(object):
    def __init__(self, id, name, mail, gender, age, phone_number, photo, owner_id):
        self.id = id
        self.name = name
        self.mail = mail
        self.gender = gender
        self.age = age
        self.phone_number = phone_number
        self.photo = photo
        self.owner_id = owner_id

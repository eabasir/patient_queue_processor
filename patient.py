from utils.status import PATIENT_STATUS
from utils.disease import default_disease_priority, diseases

from datetime import datetime

class Patient:
    def __init__(self, name, surname, national_code, disease):
        self.name = name
        self.surname = surname
        self.national_code = national_code
        self.status = PATIENT_STATUS.WAITING.value
        self.entrance_dt = datetime.now()
        self.disease = disease


    def get_priority(self):
        disease_priority = default_disease_priority
        if(self.disease in diseases):
            disease_priority = diseases[self.disease]    

        return (datetime.now().hour - self.entrance_dt.hour) / disease_priority

    def set_new_disease(self, disease):
        self.disease = disease
        self.entrance_dt = datetime.now()

    def __str__(self):
        return f"""
            Name: {self.name}
            Surname: {self.surname}
            National Code: {self.national_code}
            Status: {self.status}
            Entrance: {self.entrance_dt.hour}
            Disease: {self.disease}
            Priority: {self.get_priority()}
            -----------------------------------
        """
from pydantic import BaseModel, EmailStr, computed_field
from typing import List,Dict

class Patient(BaseModel):
    name:str
    email:EmailStr
    age:int
    weight:float
    height:float
    married:bool
    allergies:List[str]
    contact_details:Dict[str,str]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi



def insert_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.weight)
    print(patient.height)
    print('Bmi',patient.bmi)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)

    print('Data inserted in DB')


patient_info = {
    'name': 'omkar',
    'email': 'omkar@hdfc.com',
    'age': 30,
    'weight': 45,
    'height':1.12,
    'married': False,
    'allergies': ['Dust', 'Milk Products'],
    'contact_details': {
        'phone': '1234567'
    }
}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)

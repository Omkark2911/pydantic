from pydantic import BaseModel, EmailStr, model_validator
from typing import List,Dict

class Patient(BaseModel):
    name:str
    email:EmailStr
    age:int
    weight:float
    married:bool
    allergies:List[str]
    contact_details:Dict[str,str]

    @model_validator(mode='after')
    def validate_emergency_contact(cls,model):
        if model.age > 60 and 'emergency' not in model.contact_details:
           raise ValueError('Patient older than 60 must have emergency contact number.')
        return model    



def insert_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print('Data inserted in DB')

patient_info = {
    'name': 'omkar',
    'email': 'omkar@hdfc.com',
    'age': 56,
    'weight': 45,
    'married': False,
    'allergies': ['Dust', 'Milk Products'],
    'contact_details': {
        'phone': '1234567',
        'emergency':'3123456'
    }
}  

patient1 = Patient(**patient_info)

insert_patient_data(patient1)

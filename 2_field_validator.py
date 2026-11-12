

from pydantic import BaseModel, EmailStr, Field, field_validator
from typing import List, Dict

class Patient(BaseModel):

    name: str
    age: int
    email: EmailStr
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    @field_validator('email')
    @classmethod
    def email_validator(cls, value):

        valid_domains = ['hdfc.com', 'icici.com']

        domain_name = str(value).split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError('Not a valid domain')

        return value

    @field_validator('name')
    @classmethod  
    def transform_name(cls,value):
        return value.upper()


def insert_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)

    print('Data inserted in DB')


patient_info = {
    'name': 'omkar',
    'email': 'omkar@hdfc.com',
    'age': 30,
    'weight': 45,
    'married': False,
    'allergies': ['Dust', 'Milk Products'],
    'contact_details': {
        'email': 'abc@gmail.com',
        'phone': '1234567'
    }
}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)

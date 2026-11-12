from pydantic import BaseModel

class Address(BaseModel):
    city: str
    state: str
    pin: str

class Patient(BaseModel):
    name:str
    gender:str
    age:int
    address: Address

address_dict = {'city':'Mumbai', 'state':'Maharashtra','pin':'421234'}
address1 = Address(**address_dict)

patient_dict = {'name':'omkar','gender':'male','age': 22,'address':address1}
patient1 = Patient(**patient_dict)

A = patient1.model_dump() #dictionary
print(A)
print(type(A))

B = patient1.model_dump_json() #string
print(B)
print(type(B))

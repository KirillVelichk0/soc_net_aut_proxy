
from pydantic import BaseModel


class RegistrateOrLoginModel(BaseModel):
    email: str
    password: str

class VerifyModel(BaseModel):
    random_data_token: str

    
from fastapi import Query
from pydantic import BaseModel

class UserRegistrationForm(BaseModel):
    username : str
    password : str
    
class UserRegistrationResponse(BaseModel):
    id :  int
    username : str
    
    class Config:
        orm_mode = True
        
class DeleteResponse(BaseModel):
    response : dict
    
    class Config:
        orm_mode = True
        
class UserDetailsResponse(UserRegistrationResponse):
    pass

class PredictionResponse(BaseModel):
    prediction : dict
    
    class Config:
        orm_mode = True

class ModelParameter(BaseModel):
    employed: int = Query(..., ge=0, le=1)
    bank_balance: float
    annual_salary: float
    
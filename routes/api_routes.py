import sys
sys.path.append("./")

from typing import Annotated
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from fastapi.responses import JSONResponse
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from database.session import get_db
from database.create_table import TABLE
from service.api_services import API_SERVICE
from database.schema import UserRegistrationForm, UserRegistrationResponse,\
DeleteResponse, UserDetailsResponse, PredictionResponse, ModelParameter

USER_ROUTER = APIRouter(tags=["USER"])
MODEL_ROUTER = APIRouter(tags=["MODEL"])

password_hasher = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2passwordearer = OAuth2PasswordBearer(tokenUrl="/verify_user") # The token url means the path were to find the token

@USER_ROUTER.post("/register_user", response_model=UserRegistrationResponse)
async def RegisterUser(data:UserRegistrationForm, db:Annotated[Session, Depends(get_db)]):
    service = API_SERVICE(username=data.username, password=data.password)

    user = await service.GetUser(db=db)
        
    if user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User already in database")
        
    new_user = TABLE(**data.dict(exclude="password"), hashed_password=password_hasher.hash(data.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return JSONResponse(content={"message":"Account Successfully created", "details":f"user id: {new_user.id}, username: {new_user.username}"})

@USER_ROUTER.post("/verify_user")
async def AuthenticateUser(data:Annotated[OAuth2PasswordRequestForm, Depends()], db:Annotated[Session, Depends(get_db)]):
    service = API_SERVICE(username=data.username, password=data.password)
    token = await service.GetToken(db=db)
    return token

@USER_ROUTER.get("/get_user_details", response_model=UserDetailsResponse)
async def GetUserDetails(token:Annotated[str, Depends(oauth2passwordearer)], db:Annotated[Session, Depends(get_db)]):
    service = API_SERVICE()
    return await service.GetCurrentUser(token=token, db=db)
    

@USER_ROUTER.delete("/delete_user", response_model=DeleteResponse)
async def DeleteUser(token:Annotated[str, Depends(oauth2passwordearer)], db:Annotated[Session, Depends(get_db)]):
    service = API_SERVICE()
    return await service.GetCurrentUser(token=token, db=db)
      
@MODEL_ROUTER.post("/loan_default_prediction", response_model=PredictionResponse)
async def GetModelPrediction(token:Annotated[str, Depends(oauth2passwordearer)], data:ModelParameter):
    service = API_SERVICE()
    return await service.GetPrediction(data=data.dict(), token=token)
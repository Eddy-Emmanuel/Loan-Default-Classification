import sys
sys.path.append("./")

import pickle
import numpy as np
from jose import jwt, JWTError
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from datetime import datetime, timedelta
from fastapi import HTTPException, status
from fastapi.responses import JSONResponse
from config.configuration import BACKEND_CONFIG

from database.create_table import TABLE

# Load Password Hasher
password_hasher = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Load Model
with open("model\Loan_default_pred.pkl", "rb") as model_file:
    model = pickle.load(model_file)

class API_SERVICE():
    def __init__(self, username:str=None, password:str=None):
        self.username = username
        self.password = password
        
    async def GetUser(self, db:Session):
        return db.query(TABLE).filter(TABLE.username == self.username).first()
        
    async def DeleteCurrentUser(self, token:str, db:Session):
        try:
            decoded_token = jwt.decode(token,  BACKEND_CONFIG().SECRET, algorithms=BACKEND_CONFIG().ALGORITHM)
            user_id, username = decoded_token.get("user_id", None), decoded_token.get("username", None)
            
            if (not user_id) or (not username):
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Credentials")
            
            user = db.query(TABLE).filter(TABLE.id == user_id, TABLE.username == username).first()
            
            db.delete(user)
            db.commit()
            
            return JSONResponse(content={"message":"User successfully deleted"})
        
        except JWTError:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Credentials")
        
    async def GetToken(self, db:Session):
        user = db.query(TABLE).filter(TABLE.username == self.username).first()
        
        if not user:
            raise HTTPException(status_code=400, detail="User not in database")
        
        if not password_hasher.verify(secret=self.password, hash=user.hashed_password):
            raise HTTPException(status_code=400, detail="Unable to verify password.")
        
        # Note: the keys for the access token dictionary matters i.e {'access_token':'token, 'token type':token_type} if the keys are not access_token and token_type, there will be error
        return {"access_token": jwt.encode({"user_id":user.id, 
                                     "username":self.username,
                                     "exp_time":str(datetime.utcnow() + timedelta(minutes=30))}, BACKEND_CONFIG().SECRET, BACKEND_CONFIG().ALGORITHM),
                "token_type":"bearer"}
        
    async def GetCurrentUser(self, token:str, db:Session):
        try:
            decoded_token = jwt.decode(token,  BACKEND_CONFIG().SECRET, algorithms=BACKEND_CONFIG().ALGORITHM)
            user_id, username = decoded_token.get("user_id", None), decoded_token.get("username", None)
            
            if (not user_id) or (not username):
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Credentials")
            
            user = db.query(TABLE).filter(TABLE.id == user_id, TABLE.username == username).first()
            
            return user
        
        except JWTError:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Credentials")
        
    async def GetPrediction(self, token:str, data:dict):
        try:
            decoded_token = jwt.decode(token,  BACKEND_CONFIG().SECRET, algorithms=BACKEND_CONFIG().ALGORITHM)
            user_id, username = decoded_token.get("user_id", None), decoded_token.get("username", None)
            
            if (not user_id) or (not username):
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Credentials")
            
            datapoint = np.expand_dims(np.array([data['employed'], data['bank_balance'], data['annual_salary']]), axis=0)
            
             # Make prediction using the model
            prediction = model.predict(datapoint)
            
            # Map prediction to human-readable label
            output_indices = {0: "No", 1: "Yes"}
            
            prediction_label = output_indices[prediction[0]]
            
            return JSONResponse(content={"prediction" : prediction_label})
        
        except JWTError:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Credentials")
        
        
        
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from SQLFunctions import CRUD

#Create datamodel for user
class User(BaseModel):
    userID: str
    fname: str
    lname: str
    username: str
    password: str
    email: str
    deleted: Optional[int] = None

#python3 -m uvicorn users:app --reload
app = FastAPI()
print(CRUD.retrieve())
#Create User


@app.get("/user/userID")
async def createUser(user: User):
    CRUD.retrieve()
    return user
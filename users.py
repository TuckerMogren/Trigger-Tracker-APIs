from typing import Optional
from fastapi import FastAPI

from SQLFunctions import CRUD



#python3 -m uvicorn users:app --reload
app = FastAPI()
print(CRUD.retrieve())
#Create User


@app.post("/user")
async def createUser(user: User):
    CRUD.Insert(user);
    return user
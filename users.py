from os import stat
from typing import ValuesView
from fastapi import FastAPI, status, Response
from pydantic.errors import cls_kwargs
from SQLFunctions import CRUD
from Models.UserModel import User 

#python3 -m uvicorn users:app --reload
app = FastAPI()

#Create User
@app.post("/user", status_code=status.HTTP_201_CREATED)
async def createUser(user: User, res:Response):
    sql = CRUD.Insert();
    values = user.fname, user.lname, user.username, user.userID, user.email, user.deleted, user.password
    
    if CRUD.executeSQL(sql, values) == 1:
        res.status_code = status.HTTP_201_CREATED
    else:
        res.status_code = status.HTTP_400_BAD_REQUEST   
    return sql


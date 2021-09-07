from os import stat
from fastapi import FastAPI, status, Response
from SQLFunctions import CRUD
from Models.UserModel import User 

#python3 -m uvicorn users:app --reload
app = FastAPI()

#Create User
@app.post("/user")
async def createUser(user: User, res:Response):
    sql = CRUD.Insert();
    values = user.userID, user.fname, user.lname, user.username, user.password, user.email, user.deleted, 
    
    if CRUD.executeSQL(sql, values) == 1:
        res.status_code = status.HTTP_201_CREATED
    else:
        res.status_code = status.HTTP_406_NOT_ACCEPTABLE
    return sql, values, user

@app.delete("/user")
async def softDeleteUser(userID, res:Response):
    sql = CRUD.RemoveSoft()
    values = 'users', 'deleted', 'userID', userID
    if CRUD.executeSQL(sql, values) == 1:
        res.status_code = status.HTTP_202_ACCEPTED
    else:
        res.status_code = status.HTTP_406_NOT_ACCEPTABLE

    return sql, values, userID

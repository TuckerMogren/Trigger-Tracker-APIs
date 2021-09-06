from fastapi import FastAPI
from SQLFunctions import CRUD
from Models.UserModel import User 

#python3 -m uvicorn users:app --reload
app = FastAPI()
print(CRUD.retrieve())
#Create User


@app.post("/user")
async def createUser(user: User):
    CRUD.Insert(user.fname, user.lname, user.username, user.userID, user.email, user.deleted, user.deleted);
    return user
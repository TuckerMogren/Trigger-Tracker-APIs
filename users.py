from fastapi import FastAPI
from Models.UserModel import User 
from database.sqliteCreateTables import database, users

#python3 -m uvicorn users:app --reload
app = FastAPI()


#Create User
@app.post("/user/")
async def createUser(user: User):
    user.UserID = user.UserID + 432
    query = users.insert().values(userID=user.UserID, fname=user.FName, lname=user.LName, username=user.UserName, password=user.PassWord, email=user.EMail, deleted=user.Deleted)
    await database.execute(query=query)
    return {**user.dict()}



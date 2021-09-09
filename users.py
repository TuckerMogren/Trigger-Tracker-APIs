from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer
from Models.UserModel import User 
from database.sqliteCreateTables import database, users


#to run, use the following command: python3 -m uvicorn users:app --reload
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI()
#Create User
@app.post("/user/")
async def createUser(user: User):
    query = users.insert().values(userID=user.UserID, fname=user.FName, lname=user.LName, username=user.UserName, password=user.PassWord, email=user.EMail, deleted=user.Deleted)
    last_record_id = await database.execute(query)
    return {"id": last_record_id}


@app.get("/items/")
async def read_items(token: str = Depends(oauth2_scheme)):
    return {"token": token}

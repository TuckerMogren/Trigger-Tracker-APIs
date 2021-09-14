from fastapi import status, Response
from sqlite3 import Error
from pydantic import BaseModel
from typing import Optional
from fastapi.routing import APIRouter
from database.sqliteCreateTables import database, users

#Create datamodel for user
class User(BaseModel):
    UserID: int
    FName: str
    LName: str
    UserName: str
    PassWord: str
    EMail: str
    Deleted: Optional[bool] = False

# python3 -m uvicorn users:app --reload
router = APIRouter()


##This if statement will only execute if this file is being executed directly and not by any other modules if imported
#if __name__ == "__main__":
#    uvicorn.run(app, host="0.0.0.0", port=8000)

# Create User
@router.post("/api/v1/user/", tags=["users"])
async def createUser(user: User, res:Response):
    try:
        statement = users.insert().values(userID=user.UserID, fname=user.FName, lname=user.LName,
                                  username=user.UserName, password=user.PassWord, email=user.EMail, deleted=user.Deleted)
        await database.execute(query=statement)
    except Error as e:
        res.status_code = status.HTTP_400_BAD_REQUEST
        return [{"Status": res.status_code}, {"UserID": user.UserID, "Username":user.UserName}, {"ErrorMessage":e.args}]
    res.status_code = status.HTTP_201_CREATED
    return {"Status": res.status_code, "UserID": user.UserID}


@router.get("/api/v1/user/{userID}", tags=["users"])
async def getUser(userID, res:Response):
    try:
        statement = users.select().where(users.c.userID == userID)
        results = await database.fetch_all(query=statement)
        if results == []:
            raise AssertionError()
    except AssertionError as e:
        res.status_code = status.HTTP_404_NOT_FOUND
        return [{"Status": res.status_code}, {"ErrorMessage":"No data found in database for userID: " + userID}]
    except Error as e:
        res.status_code = status.HTTP_400_BAD_REQUEST
        return [{"Status": res.status_code}, {"ErrorMessage":e.args}]
    res.status_code = status.HTTP_200_OK
    return [{"Status": res.status_code}, {"UserID":userID}, {"results":results} ]


@router.patch("/api/v1/User/{userID}", tags=["users"])
async def softDeleteUser(userID, res:Response):
    try:
        statement = users.update().where(users.c.userID == userID).values(deleted=True)
        results = await database.execute(statement)
    except Error as e:
        res.status_code = status.HTTP_400_BAD_REQUEST
        return [{"Status": res.status_code}, {"ErrorMessage":e.args}]
    res.status_code = status.HTTP_202_ACCEPTED
    return [{"Status": res.status_code}, {"UserID":userID}, {"results":results} ]


from fastapi import FastAPI, status, Response
from sqlite3 import Error
from Models.UserModel import User
from database.sqliteCreateTables import database, users


# python3 -m uvicorn users:app --reload
app = FastAPI()


##This if statement will only execute if this file is being executed directly and not by any other modules if imported
#if __name__ == "__main__":
#    uvicorn.run(app, host="0.0.0.0", port=8000)

# Create User
@app.post("/api/v1/user/")
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


@app.get("/api/v1/user/{userID}")
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


@app.patch("/api/v1/User/{userID}")
async def softDeleteUser(userID, res:Response):
    try:
        statement = users.update().where(users.c.userID == userID).values(deleted=True)
        results = await database.execute(statement)
    except Error as e:
        res.status_code = status.HTTP_400_BAD_REQUEST
        return [{"Status": res.status_code}, {"ErrorMessage":e.args}]
    res.status_code = status.HTTP_202_ACCEPTED
    return [{"Status": res.status_code}, {"UserID":userID}, {"results":results} ]


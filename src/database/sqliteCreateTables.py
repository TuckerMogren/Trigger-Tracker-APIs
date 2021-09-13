import databases
from sqlalchemy import Column, Integer, String, MetaData, create_engine, Table, BLOB, Boolean, DateTime, ForeignKey
from fastapi import FastAPI


databaseName = '../database/TriggerTracker'
# connectionName = 'sqlite:///./' + databaseName + '.db' #currently incorrect as file has been moved

DATABASE_URL = 'sqlite:///' + databaseName + '.db'

database = databases.Database(DATABASE_URL)


metadata = MetaData()


# reference: https://github.com/Logicmn/PYX/blob/master/PYX.py


users = Table(
    "users",
    metadata,
    Column("userID", Integer, primary_key=True),
    Column("fname", String, nullable=False),
    Column("lname", String, nullable=False),
    Column("username", String, nullable=False),
    Column("password", String, nullable=False),
    Column("email", String, nullable=False),
    Column("deleted", Boolean, nullable=False)

)

photos = Table(
    "photos",
    metadata,
    Column("photoID", Integer, primary_key=True),
    Column("userID", Integer, ForeignKey('users.userID'), nullable=False),
    Column("photo", String, nullable=False),
    Column("photoTimeStamp", DateTime, nullable=False),
    Column("entryText", String, nullable=False),
    Column("deleted", Boolean, nullable=False)

)
#will only recreate database if this file is directly ran via python3 sqliteCreateTables command
if __name__ == "__main__":
    engine = create_engine(

        DATABASE_URL, echo=False, connect_args={"check_same_thread": False}
    )

    metadata.create_all(engine)

app = FastAPI()


@app.on_event("startup")
async def startup():
    print("Application is starting..... Connecting to database.")
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    print("Application is shuting down..... disconnecting from database.")
    await database.disconnect()

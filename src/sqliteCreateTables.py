from typing import List
import databases
from sqlalchemy import Column, Integer, String, MetaData, create_engine, Table, BLOB, Boolean, TIME, ForeignKey
from fastapi import FastAPI


databaseName  = '../database/TriggerTracker'
#connectionName = 'sqlite:///./' + databaseName + '.db' #currently incorrect as file has been moved

DATABASE_URL = 'sqlite:///' + databaseName + '.db'

database = databases.Database(DATABASE_URL)


metadata = MetaData()


#reference: https://github.com/Logicmn/PYX/blob/master/PYX.py

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
    Column("userID", Integer, ForeignKey('users.userID'), nullable=False ),
    Column("photo", BLOB, nullable=False),
    Column("photoTimeStamp", TIME, nullable=False),
    Column("entryText", String, nullable=False),
    Column("deleted", Boolean, nullable=False)

)

engine = create_engine(

    DATABASE_URL, echo = True, connect_args={"check_same_thread": False}
)

metadata.create_all(engine)

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
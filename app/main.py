#https://fastapi.tiangolo.com/tutorial/bigger-applications/
from fastapi import Depends, FastAPI
from dependencies import get_query_token
from .routers import users, photos
from .routers.database.sqliteCreateTables import *

app = FastAPI(dependencies=[Depends(get_query_token)])

app.include_router(users.router)
app.include_router(photos.router)





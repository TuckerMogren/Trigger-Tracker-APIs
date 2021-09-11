from datetime import time
from pydantic import BaseModel
from typing import Optional


#Create datamodel for photos
class User(BaseModel):
    photoID: int
    userID: int
    photo: str
    photoTimeStamp: time
    entryText: str
    deleted: Optional[bool] = None
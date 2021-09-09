from pydantic import BaseModel
from typing import Optional


#Create datamodel for user
class User(BaseModel):
    UserID: int
    FName: str
    LName: str
    UserName: str
    PassWord: str
    EMail: str
    Deleted: Optional[bool] = False
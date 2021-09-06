from pydantic import BaseModel

#Create datamodel for user
class User(BaseModel):
    userID: str
    fname: str
    lname: str
    username: str
    password: str
    email: str
    deleted: Optional[int] = None
from datetime import datetime
from pydantic import BaseModel
from typing import Optional

from sqlalchemy.sql.sqltypes import BLOB


#Create datamodel for photos
class Photo(BaseModel):
    photoID: int
    userID: int
    photo: str
    photoTimeStamp: datetime
    entryText: str
    deleted: Optional[bool] = False


    #https://stackoverflow.com/questions/68893175/error-value-not-declarable-with-json-schema-for-purepath-with-pydantic-and-fasta
    #required for the use of SQL BLOB and DateTime
    class Config:
        arbitrary_types_allowed = True

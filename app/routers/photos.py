from fastapi import status, Response, APIRouter
from sqlite3 import Error
from database.sqliteCreateTables import database, photos
from datetime import datetime
from pydantic import BaseModel
from typing import Optional

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


router = APIRouter()


@router.post("/api/v1/photo/", tags=["photos"])
async def createPhoto(photo: Photo, res: Response):
    try:
        statement = photos.insert().values(photoID=photo.photoID, userID=photo.userID, photo=photo.photo,
                                           photoTimeStamp=photo.photoTimeStamp, entryText=photo.entryText, deleted=photo.deleted)
        await database.execute(query=statement)
    except Error as e:
        res.status_code = status.HTTP_400_BAD_REQUEST
        return [{"Status": res.status_code}, {"PhotoID": photo.photoID, "UserID": photo.userID}, {"ErrorMessage": e.args}]
    res.status_code = status.HTTP_201_CREATED
    return {"Status": res.status_code, "PhotoID": photo.photoID, "UserID": photo.userID}


@router.get("/api/v1/photo/{photoID}", tags=["photos"])
async def getPhoto(photoID, res: Response):
    try:
        statement = photos.select(photos.c.userID).where(photos.c.photoID == photoID)
        results = await database.fetch_one(query=statement)
        if results == []:
            raise AssertionError()
    except AssertionError as e:
        res.status_code = status.HTTP_404_NOT_FOUND
        return [{"Status": res.status_code}, {"ErrorMessage":"No data found in database for photoID: " + photoID}]
    except Error as e:
        res.status_code = status.HTTP_400_BAD_REQUEST
        return [{"Status": res.status_code}, {"ErrorMessage":e.args}]
    except:
        res.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"Message":"Unknown, fatal error"}
    res.status_code = status.HTTP_200_OK
    return [{"Status": res.status_code}, {"PhotoID":photoID}, {"Photo":photos.c.photo} ]


from SQLFunctions import CRUD
from Models.UserModel import User
from sqliteCreateTables import cursor, connection

User.userID = 1
User.fname = "Tucker"
User.lname = "Mogren"
User.username = "Mogrent"
User.password = "helloworld!"
User.email = "mogrent@hotmail.com"
User.deleted = 0

sql = CRUD.RemoveSoft()
values = 'users', 'deleted', 'userID', User.userID
print(sql, values)

cursor.execute("UPDATE users SET deleted = 0 WHERE userID = 1")


('UPDATE :tableName SET :col = :value WHERE :field = :userID', {"tableName":'users', })
connection.commit()
print(cursor.fetchall())
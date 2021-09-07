from SQLFunctions import CRUD
from Models.UserModel import User
from database.sqliteCreateTables import cursor, connection

User.userID = 21
User.fname = "Tucker"
User.lname = "Mogren"
User.username = "Mogrent"
User.password = "helloworld!"
User.email = "mogrent@hotmail.com"
User.deleted = 0


sql = (CRUD.Insert())

cursor.execute(sql, (User.userID, User.fname, User.lname, User.username, User.password, User.email, User.deleted))
#cursor.execute("INSERT INTO users VALUES(?, ?, ?, ?, ?, ?, ?)",(20, 'Tucker', 'Mogren', 'Mogrent', 'helloworld!', 'mogrent@hotmail.com', 0))
connection.commit()

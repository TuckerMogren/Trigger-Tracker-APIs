from Models.UserModel import User
from database.sqliteCreateTables import cursor, connection, Error

class CRUD():
    def __init__(self, user:User):
        self.First = user.fname
        self.Last = user.lname
        self.UserID = user.userID
        self.UserName = user.username
        self.PassWord = user.password
        self.EMail = user.email
        self.Deleted = user.deleted

    def retrieve():
        print("Read")
    def Insert():
        sql = 'INSERT INTO users VALUES(?, ?, ?, ?, ?, ?, ?)'
        return (sql)
    def RemoveSoft():
        print("Soft Remove")
    def RemoveHard():
        print("Hard Remove")
    def Update():
        print("Update")

    def executeSQL(statement):
        print("In EXECUTE" + statement)
        try:
            cursor.execute()
            connection.commit()
            return 1
        except Error as e:
            print(e)
            return 0
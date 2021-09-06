from database.sqliteCreateTables import cursor, connection
class CRUD():
    def retrieve():
        print("Read")
    def Insert(Fname, Lname, Username, Userid, Email, Deleted, Password):
        sql = ('''INSERT INTO users(userID, fname, lname,username, password, email, deleted) VALUES(Fname, Lname, Username, Userid, Email, Deleted, Password)''')
        return sql
    def RemoveSoft():
        print("Soft Remove")
    def RemoveHard():
        print("Hard Remove")
    def Update():
        print("Update")

    def executeSQL(statement):
        try:
            cursor.execute(statement)
            connection.commit()
            return 0
        except:
            connection.close()
            return 1
from sqlite3.dbapi2 import Cursor
from database import sqliteCreateTables

Cursor.execute("INSERT INTO users VALUES (1, 'Tucker', 'Mogren', 'mogrent', 'mogrent@hotmail.com', 'thisisatest', 0)")




import sqlite3
databaseName  = 'TriggerTracker'
connectionName = 'database/' + databaseName + '.db'
connection = sqlite3.connect(connectionName)
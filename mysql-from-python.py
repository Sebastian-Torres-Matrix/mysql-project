import os
import datetime
import pymysql

# Get username from workspace
# modify this variable if runnin on another environment
username = os.getenv('C9_USER')

# Connect to database
connection = pymysql.connect(host='localhost', user = username, password = '', db = 'Chinook')

try:
    # Run a query
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        sql = "SELECT * FROM Genre;"
        cursor.execute("""CREATE TABLE IF NOT EXISTS
                        Friends(name char(20), age int, DOB datetime);""")
        # Note that the above will still display a warning (not error) if the 
        # table already exists
        for row in cursor:
            print(row)
finally:
        #Close the connection, regardless of wheter the above was succesful
        connection.close()

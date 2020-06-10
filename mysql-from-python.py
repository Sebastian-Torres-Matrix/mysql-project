import os
import pymysql

# Get username from workspace
# modify this variable if runnin on another environment
username = os.getenv('C9_USER')

# Connect to database
connection = pymysql.connect(host='localhost', user = username, password = '', db = 'Chinook')

try:
    # Run a query
    with connection.cursor() as cursor:
        sql = "SELECT * FROM Artist;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
        #Close the connection, regardless of wheter the above was succesful
        connection.close()

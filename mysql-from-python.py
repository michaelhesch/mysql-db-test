import os
import pymysql

# Get username from workspace
# (modify if running on another environment)
username = os.getenv('GITPOD_USER_NAME')

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user=username,
                             password='',
                             db='Chinook')

try:
    # Run a query
    with connection.cursor() as cursor:
        sql = "SELECT * FROM Artist;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    # close the db connection, regardless of what happens
    connection.close()


import os
import datetime
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
    with connection.cursor() as cursor:
        list_of_names = ['fred', 'Fred']
        # Prepare a string with same number of placeholders as in list_of_names
        format_strings = ','.join(['%s'] * len(list_of_names))
        cursor.execute(
            "DELETE FROM Friends WHERE name in ({});".format(format_strings),
            list_of_names)

        # Update multiple rows using list of tuples and executemany
        # rows = [(23, 'Bob'),
        #        (24, 'Jim'),
        #        (25, 'Fred')  
        # ]
        # cursor.executemany("UPDATE Friends SET age = %s WHERE name = %s;",
        #                   rows)
        # Update table using string interpolation
        # cursor.execute("UPDATE Friends SET age = %s WHERE name = %s;",
        #                (23, 'Bob'))
        # Insert multiple rows using list of tuples and executemany method
        # rows = [("Bob", 21, "1990-02-06 23:04:50"),
        #        ("Jim", 56, "1955-05-09 13:12:45"),
        #        ("Fred", 100, "1911-09-12 01:01:01")]
        # cursor.executemany("INSERT INTO Friends VALUES (%s, %s, %s);", rows)
        # Creates new table with given attributes for each column
        # cursor.execute("""CREATE TABLE IF NOT EXISTS
        #                  Friends(name char(20), age int, DOB datetime);""")
        # Note that the above will still display a warning (not error) if the
        # table already exists
        connection.commit()
finally:
    connection.close()

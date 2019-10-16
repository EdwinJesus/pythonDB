import pyodbc 

conn = pyodbc.connect(
                      'Driver={SQL Server};'
                      'Server=192.168.10.100;'
                      'Database=example;'
                      'uid=user2019;pwd=xxxxxxx')


cursor = conn.cursor()

cursor.execute('Select * From Table Where Area = 6')

for row in cursor:
    print(row)

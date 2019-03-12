import pyodbc
import datetime

server = 'esp32-temp.database.windows.net'
database = 'weather'
username = 'thiemo.seys'
password = 'lookroker13!'
driver= '{ODBC Driver 13 for SQL Server}'
cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()



#fetching all results
def get_all():
    cursor.execute("SELECT * FROM measurements")
    row = cursor.fetchone()
    while row:
        print (str(row[0]) + " " + str(row[1]))
        row = cursor.fetchone()

def add_measurement(deviceID, temp, hum):
    cursor.execute("INSERT INTO measurements(time,DeviceID,temp,hum) VALUES(?,?,?,?)",datetime.datetime.now() ,deviceID, temp, hum )
    cnxn.commit()
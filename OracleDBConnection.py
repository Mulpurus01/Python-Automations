#!pip install oracledb
#!py -m pip install oracledb

import oracledb

username='USERNAME'
password='PASSWORD'
hostname='HOSTNAME'
port="portnumber" #Number / integer
serviceName='SERVICE_NAME'

dataSourceName=oracledb.makedsn(hostname,port,service_name=serviceName)
dbConnection=oracledb.connect(username,password,dataSourceName)
cursor=dbConnection.cursor()

QUERY='SELECT COLUMN1 FROM TABLE'
cursor.execute(QUERY)
resultSet=cursor.fetchall()

for row in resultSet:
  print(row)

cursor.close()
dbConnection.close()

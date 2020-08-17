import json
import pymssql
from ssm_parameter_store import EC2ParameterStore

store = EC2ParameterStore()


server_pass = store.get_parameter('db_pass', decrypt=True)
server_host = store.get_parameter('db_host', decrypt=True)
server_user = store.get_parameter('db_user', decrypt=True)
server_db   = store.get_parameter('db_database', decrypt=True)


server   = server_host["db_host"]
username = server_user["db_user"]
password = server_pass["db_pass"]
database = server_db["db_database"]

try:
   Db = pymssql.connect(server,username,password)    
except (pymssql.InterfaceError,pymssql.OperationalError):
  print("Failed to Connect to Server")
else:
   print("Successful Connection to Server")








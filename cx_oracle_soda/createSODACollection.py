import configparser
import cx_Oracle
import json
import requests

config = configparser.ConfigParser()
config.read('C:/Users/shobhit/Documents/Python/Config/config.txt')

hostname =  config.get("DB_CONN_DETAILS","hostname")
port =  config.get("DB_CONN_DETAILS","port")
servicename =  config.get("DB_CONN_DETAILS","servicename")
username =  config.get("DB_CONN_CRED","username")
password =  config.get("DB_CONN_CRED","password")
encoding = config.get("DB_CONN_DETAILS","encoding")

print('Starting session...')
try:
    dsn = cx_Oracle.makedsn(hostname, port, service_name=servicename)
    conn = cx_Oracle.connect(username,password,dsn,encoding=encoding)
    print('Connected:' + conn.version)
 
    soda = conn.getSodaDatabase()
    collection = soda.createCollection("first_collection")
    conn.close()
    print('connection closed...')
except cx_Oracle.Error as e:
    print('Error:', e)
        
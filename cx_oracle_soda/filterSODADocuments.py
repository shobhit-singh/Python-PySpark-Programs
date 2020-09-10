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
    coll = soda.openCollection("first_collection")
    doc = coll.find()    
    docs = doc.filter({"Numbers": {"0": "Zero", "1": "One"}})
    #docs = doc.filter({"name": "BigDataEnthusiast"})
 
    print( 'Count' ,docs.count())
    print( 'Doc Key:' , docs.getDocuments())
 
    conn.close()
    print('connection closed...')
except cx_Oracle.Error as e:
    print('Error:', e)

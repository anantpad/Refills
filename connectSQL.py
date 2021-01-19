import os

import pyodbc
from dotenv import load_dotenv


def get_conn_str():
    load_dotenv('.env')
    server = os.getenv("SERVER")
    database = os.getenv("DATABASE")
    uid = os.getenv("UID")
    pwd = os.getenv("PWD")
    conn_str = (
            'DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + uid + ';PWD=' + pwd + ';Trusted_Connection=No;')
    cnxn = pyodbc.connect(conn_str)
    return cnxn


def connectSQL(cnxn):
    cursor = cnxn.cursor()
    return cursor
    # for row in cursor.execute('select DISTINCT first,last from PatientProfile'):
    #     print(row.first)


def closeConn(cnxn, cursor):
    cursor.close()
    cnxn.close()


def executeScriptsFromFile(fileName):
    fd = open(fileName, 'r')
    sqlfile = fd.read()
    fd.close()
    sqlCommands = sqlfile.split(';')
    for command in sqlCommands:
        data = cursor.execute(command).fetchall()
        final_data = [list(i) for i in data]
        return final_data

connStr = get_conn_str()
cursor = connectSQL(connStr)
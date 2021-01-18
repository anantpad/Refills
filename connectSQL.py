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


def get_pat_name(cursor):
    data = cursor.execute(
        'select distinct r.RcopiaIdentifier,p.PTID,m.MID,u.FIRSTNAME,u.LASTNAME,u.NPI,l.ADDRESS1,l.CITY,l.STATE,l.ZIP,l.PRIMPHONE,l.FAXPHONE,pp.First,pp.last,pp.Sex,pp.Birthdate,pp.Address1,pp.City,pp.State,pp.Zip,pp.Phone1,m.DESCRIPTION,CONCAT(m.NDCLABPROD,m.NDCPACKAGE) as NDCID,p.QUANTITY,m.INSTRUCTIONS from RcopiaMapPrescription r '
        'JOIN PRESCRIB p on p.PTID = r.CentricityIdentifier '
        'JOIN MEDICATE m on m.MID = p.MID '
        'JOIN DDID_RXNORM rx on rx.DDID = m.DDID '
        'JOIN NDCTODDID ndc on ndc.DDID = m.DDID '
        'JOIN PatientProfile pp on pp.PId = p.PID '
        'JOIN USR u on u.PVID = p.PUBUSER '
        'JOIN DOCUMENT d on d.SDID = p.SDID '
        'JOIN LOCREG l on l.LOCID = d.LOCOFCARE '
        'WHERE r.IsDeleted != \'Y\';').fetchall()
    return data


def useData(data):
    return data


connStr = get_conn_str()
cursor = connectSQL(connStr)
for i in get_pat_name(cursor):
    print(i[15])
closeConn(connStr, cursor)

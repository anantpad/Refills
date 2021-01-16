import pyodbc

conn_str = (
    'Trusted_Connection=No;'
    'driver={SQL Server};'
    'server=DEMOCPS00362001.englab.athenahealth.com;'
    'database=demodb;'
    'uid=sa;'
    'pwd=GEps2006;'
)
cnxn = pyodbc.connect(conn_str)

cursor = cnxn.cursor()

for row in cursor.execute('select DISTINCT first,last from PatientProfile'):
    print(row.first)

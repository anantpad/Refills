from connectSQL import *

data = executeScriptsFromFile('sqlCommand.sql')
patientData = executeScriptsFromFile('patient.sql')

for i in data:
    print(i)

for i in patientData:
    print(i)

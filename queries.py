from connectSQL import *

data = executeScriptsFromFile('sqlCommand.sql')
patientData = executeScriptsFromFile('patient.sql')
list = []
for i in data:
    if "661" in i[5]:
        list.append(i[0])
print(list[0])

# for i in patientData:
#     print(i)

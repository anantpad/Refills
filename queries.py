from connectSQL import *

data = executeScriptsFromFile('sqlCommand.sql')
for i in data:
    print(i)

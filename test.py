import os
import datetime

dirpath = datetime.datetime.today().isoweekday()
dirpath = str(dirpath)
os.chdir(os.getcwd() + '\\menu\\' + dirpath)
print(os.getcwd())

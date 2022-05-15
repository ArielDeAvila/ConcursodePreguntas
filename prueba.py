from asyncore import write
import csv
from dataclasses import field  

info = {}

info["name"] = "Ariel"
info["count"] = 5
info["acumulado"] = 1500


with open('files/history.csv','w') as historyFile:
    fieldnames = ['name','count','acumulado']
    write = csv.DictWriter(historyFile,fieldnames=fieldnames)
    write.writerow(info)


import csv
from csv import DictReader

class historyResults():
    def __init__(self,player=None):
        self.player = player
        self.saveInfo()
        self.saveMatch()
        
    def saveInfo(self):
        self.infoToSave = {}
        self.infoToSave["name"] = self.player.info["name"]
        self.infoToSave["count"] = self.player.info["count"]
        self.infoToSave["acumulado"] = self.player.info["acumulado"]
    
    def saveMatch(self):
        with open('files/history.csv', 'a',newline='') as historyFile:
            fieldnames = ['name', 'count', 'acumulado']
            write = csv.DictWriter(historyFile, fieldnames=fieldnames,dialect='excel')
            write.writerow(self.infoToSave)
            historyFile.close()
        
      
    
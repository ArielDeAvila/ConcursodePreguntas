import csv

class historyMatch():
    def __init__(self):
        self.listPlayer= []
        self.readHistory()
    
    def readHistory(self):
        with open("files/history.csv") as file:
            reader = csv.reader(file, delimiter=',')
            for row in reader:
                self.listPlayer.append(row)

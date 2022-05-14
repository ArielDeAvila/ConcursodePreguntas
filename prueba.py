from ast import List
import random

def orderQuestion():
    lists = [1, 2, 3, 4]
    for i in range(3):
        random.shuffle(lists)
        print(lists)

num = orderQuestion()

#print(type(num))
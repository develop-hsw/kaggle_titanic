import csv
import os

path = "D:/titanic"


def loader():
    f_test = open(path+"/test.csv", 'r', encoding="utf-8")
    reader = csv.reader(f_test)
    for line in reader:
        print(line)
    f_test.close()

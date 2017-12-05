import pygal as pg
import csv
def tri_rate(obj):
    reader = csv.DictReader(obj, delimiter = ',')
    for line in reader:
        for i in line:
            print(i, line[i])

def main():
    with open("../Data/Data.csv") as obj:
        tri_rate(obj)
main()


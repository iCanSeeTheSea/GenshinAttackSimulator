import csv

data = {}

with open('base reaction dmg.txt', 'r') as f:
    reader = csv.reader(f, delimiter=',')

    for line in reader:

        level = line.pop(0)
        data[level] = line[1]

print(data)

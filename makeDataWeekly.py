import csv

"""
def appendToCSV(row):
    with open('weekly-1983-Present.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(row)

with open('weekly-1983-Present.csv', 'w') as f:
    writer = csv.writer(f)


with open('dataset-1983-Present.csv', 'r') as f:
     reader = csv.reader(f, delimiter=',')
     counter = 0
     firstTime = True
     for row in reader:
        if firstTime:
            firstTime = False
            appendToCSV(row)
        elif counter == 0:
            counter = 6
            appendToCSV(row)
        else:
            counter -= 1

print("done")
"""

"""
def appendToCSV(row):
    with open('weekly-1991-Present.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(row)

with open('weekly-1991-Present.csv', 'w', newline='') as f:
    writer = csv.writer(f)

with open('dataset-1991-Present.csv', 'r') as f:
     reader = csv.reader(f, delimiter=',')
     counter = 0
     firstTime = True
     for row in reader:
        if firstTime:
            firstTime = False
            appendToCSV(row)
        elif counter == 0:
            counter = 6
            appendToCSV(row)
        else:
            counter -= 1

print("done")
"""
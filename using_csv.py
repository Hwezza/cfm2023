#retired:
import csv
data = []
with open('cfmtestSpreadsheet.csv') as csv_file:
    csv_read=csv.reader(csv_file, delimiter=',')

    for line in csv_file:
        data.append(line.strip().split(","))

for line in data:
    print(line)


import csv
import math

with open("data.csv", newline = "") as f:
    reader = csv.reader(f)
    fileData = list(reader)

    data = fileData[0]

def mean(data):
    n = len(data)
    total = 0
    for x in data:
        total = total + int(x)
    mean = total/n
    return mean

sqList = []
for number in data:
    a = int(number) - mean(data)
    a = math.pow(a,2)
    sqList.append(a)

sum = 0
for i in sqList:
    sum = sum + i 

result = sum/(len(data) - 1)

stddev = math.sqrt(result)
print(stddev)

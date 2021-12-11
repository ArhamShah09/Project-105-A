import csv
import math

with open('data.csv', newline = '') as f:
    reader = csv.reader(f)
    file_data = list(reader)

data = file_data[0]

n = len(data)

total = 0

for x in data:
    total = total + int(x)

mean = total/n

print(mean)

squared_list = []

for number in data:
    a = int(number) - mean
    a = a**2
    squared_list.append(a)

sum = 0

for i in squared_list:
    sum = sum+i

result = sum/n-1
std_dev = math.sqrt(result)

print(std_dev)
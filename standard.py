import math
import csv

with open('deviation.csv') as f:
    reader = csv.reader(f)
    data = list(reader)

total = 0

for number in data:
   total += int(number)

mean = total/len(data)

squares = []

for number in data:
    square = (int(number) - mean)**2
    squares.append(square)

sigma = 0

for everysquare in squares:
    sigma += everysquare

result = sigma/(len(data) - 1)

std_deviation = math.sqrt(result)
print(std_deviation)
import re

file = open("regex_sum_902763.txt")

temp = list()
for line in file:
    data = re.findall('[0-9]+',line)
    temp = temp + data

sum = 0
for i in temp:
    sum = sum + int(i)

print(sum)
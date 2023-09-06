#!/usr/bin/python3
result = ""
for i in range(10):
    for j in range(i + 1, 10):
        result += "{0}{1}, ".format(i, j)
print(result[:-2])

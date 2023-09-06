#!/usr/bin/python3
output = ""
for i in range(100):
    output += "{:02d}, ".format(i)

print(output.rstrip(", "))

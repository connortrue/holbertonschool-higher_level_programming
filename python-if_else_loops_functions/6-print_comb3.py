#!/usr/bin/python3
digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
output = ""
for i in range(len(digits)):
    for j in range(i + 1, len(digits)):
        if digits[i] < digits[j]:
            output += f"{digits[i]}{digits[j]:02d}", end=", "

print(output.rstrip(", "))

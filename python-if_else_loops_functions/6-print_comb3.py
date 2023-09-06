#!/usr/bin/python3
digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
result = []

for i in range(len(digits)):
    for j in range(i + 1, len(digits)):
        if digits[i] < digits[j]:
            result.append("{0}{1:02d}".format(digits[i], digits[j]))

print(", ".join(result))

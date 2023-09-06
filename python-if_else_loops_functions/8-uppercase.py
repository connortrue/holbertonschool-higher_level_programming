#!/usr/bin/python3
def uppercase(s):
    result = ""
    for c in s:
        if ord(c) >= 97 and ord(c) <= 122:
            result += "{0}".format(chr(ord(c) - 32))
        else:
            result += "{0}".format(c)
    print(result)

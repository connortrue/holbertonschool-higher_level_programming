#!/usr/bin/python3
class MyList(list):
    def print_sorted(self):
        for i in sorted(self):
            print(i)

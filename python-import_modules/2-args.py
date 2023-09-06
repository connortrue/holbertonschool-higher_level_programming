#!/usr/bin/python3
import sys


def main():
    num = len(sys.argv) - 1
    
    if num >= 1:
        print("{:d} arguments:".format(num))
        for i in range(1, num + 1):
            print("{:d}: {:s}".format(i, sys.argv[i]))


if __name__ == "__main__":
    main()

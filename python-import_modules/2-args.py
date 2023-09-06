#!/usr/bin/python3
import sys

def print_args():
    args = sys.argv[1:]
    num_args = len(args)
    print(f"Number of argument{'s' if num_args != 1 else ''}: {num_args}")
    for i, arg in enumerate(args):
        print(f"{i+1}: {arg}")

if __name__ == "__main__":
    print_args()

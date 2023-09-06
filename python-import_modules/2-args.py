import sys

def print_args():
    args = sys.argv[1:]
    num_args = len(args)
    print(f"{num_args} argument{'s' if num_args != 1 else ''}:")
    for i, arg in enumerate(args):
        print(f"{i+1}: {arg}")

if __name__ == "__main__":
    print_args()

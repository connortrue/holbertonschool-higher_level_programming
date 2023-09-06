import hidden_4


def print_names():
    """Prints names defined by the compiled module hidden_4.pyc"""
    names = dir(hidden_4)
    for name in sorted(names):
        if not name.startswith("__"):
            print(name)


if __name__ == "__main__":
    print_names()


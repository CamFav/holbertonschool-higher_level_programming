#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    names = dir(hidden_4)
    sorted_names = [name for name in names if not name.startswith("__")]
    sorted_names = sorted(sorted_names)

    for name in sorted_names:
        print(name)

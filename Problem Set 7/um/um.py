import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    um_counter = re.findall(r"\bum\b", s, re.IGNORECASE)
    return len(um_counter)


if __name__ == "__main__":
    main()

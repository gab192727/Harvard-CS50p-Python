import re
import sys

def main():
    print(count(input("Text: ")))


def count(input):

    matches = re.findall(r'\bum\b', input, re.IGNORECASE)
    return len(matches)


if __name__ == "__main__":
    main()

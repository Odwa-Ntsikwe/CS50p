import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if url := re.search(r"^<iframe.+https?://(?:www\.)?youtube\.com/embed/([a-z0-9]+).+></iframe>$", s, re.IGNORECASE):
        return f"https://youtu.be/{url.group(1)}"


if __name__ == "__main__":
    main()

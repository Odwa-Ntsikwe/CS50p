import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    valid_address = re.search(r"^([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$", ip)

    if valid_address:
        for i in range(1, 5):
            if int(valid_address.group(i)) > 255:
                return False
        return True
    else:
        return False

if __name__ == "__main__":
    main()

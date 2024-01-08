import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    match = re.search(r"^([0-9]{1,2}):?([0-9]{2})? (AM|PM) to ([0-9]{1,2}):?([0-9]{2})? (AM|PM)$", s, re.IGNORECASE)
    if match:
        if int(match.group(1)) and int(match.group(4)) > 12:
            raise ValueError
        time1 = time_format(match.group(1), match.group(2), match.group(3))
        time2 = time_format(match.group(4), match.group(5), match.group(6))
        return f"{time1} to {time2}"
    else:
        raise ValueError

def time_format(hours, minutes, meridiem):
    if meridiem == "PM" and int(hours) != 12:
        hrs = int(hours) + 12
    elif meridiem == "AM" and int(hours) == 12:
        hrs = 0
    else:
        hrs = int(hours)


    if minutes == None:
        min = "00"
    elif int(minutes) > 59:
        raise ValueError
    else:
        min = f"{int(minutes):02}"
    return f"{hrs:02}:{min}"

if __name__ == "__main__":
    main()

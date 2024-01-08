from datetime import date
import operator
import inflect
import sys

p = inflect.engine()

def convert_age_to_minutes(year, month, day):
    dob = date(int(year), int(month), int(day))
    difference = operator.__sub__(date.today(), dob)
    minutes = difference.days * 24 * 60
    return f"{p.number_to_words(minutes, andword='').capitalize()} minutes"

def main():
    try:
        dob = input("Date of Birth: ")
        year, month, day = dob.split("-")
        print(convert_age_to_minutes(year, month, day))

    except ValueError:
        sys.exit("Invalid date")


if __name__ == "__main__":
    main()



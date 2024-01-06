def main():
    period = input("What time is it? ")

    if convert(period) >= 7.0 and convert(period) <= 8.0:
        print("breakfast time")
    if convert(period) >= 12.0 and convert(period) <= 13.0:
        print("lunch time")
    if convert(period) >= 18.0 and convert(period) <= 19.0:
        print("dinner time")

def convert(time):
    hours, minutes = time.split(":")
    new_hours = float(hours)
    new_minutes = float(minutes)
    new_minutes = new_minutes/60
    return new_hours + new_minutes


if __name__ == "__main__":
    main()

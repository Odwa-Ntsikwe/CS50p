months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        date = input("Date: ")
        if "/" in date:
            month, day, year = date.split("/")
        elif "," in date:
            date = date.replace(",", "")
            month, day, year = date.split(" ")
            for i in range(len(months)):
                if month == months[i]:
                    month = i + 1
        month, day = int(month), int(day)

        if (month >= 1 and month <= 12) and (day >= 1 and day <= 31):
            break

    except:
        print()
        pass

print(f"{int(year)}-{int(month):02}-{int(day):02}")

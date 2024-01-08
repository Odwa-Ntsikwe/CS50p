import sys
import csv

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
if ".csv" not in (sys.argv[1][-4:] and sys.argv[2][-4:]):
    sys.exit("Nots a CSV file")
students = []

try:
    with open(sys.argv[1], "r") as read_file:
        reader = csv.DictReader(read_file)
        for row in reader:
            names = row["name"].split(",")
            students.append({"first": names[1].lstrip(), "last": names[0], "house": row["house"]})

    with open(sys.argv[2], "w") as file:
        writer = csv.DictWriter(file, fieldnames = ["first","last","house"])
        writer.writeheader()
        for student in students:
            writer.writerow({"first": student["first"], "last": student["last"], "house": student["house"]})

except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")

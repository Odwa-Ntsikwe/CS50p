import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
if ".py" not in sys.argv[1][-3:]:
    sys.exit("Not a Python file")

try:
    counter = 0
    with open(sys.argv[1], "r") as file:
        for line in file:
            if not(line.lstrip().startswith("#") or line.lstrip() == ""):
                counter += 1
        print(counter)

except FileNotFoundError:
    sys.exit("File does not exist")



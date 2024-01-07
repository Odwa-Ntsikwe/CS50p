import random


def main():
    level = get_level()
    score = 0
    for _ in range(10):
        attempts = 0
        x, y = generate_integer(level)
        while True:
            if attempts == 3:
                print(f"{x} + {y} = {x + y}")
                break
            try:
                answer = int(input(f"{x} + {y} = "))
            except ValueError:
                attempts += 1
                print("EEE")
            else:
                if answer == x + y:
                    score += 1
                    break
                else:
                    attempts += 1
                    print("EEE")
    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level == 1 or level == 2 or level == 3:
                return level
        except:
            pass


def generate_integer(level):
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    else:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
    return x, y


if __name__ == "__main__":
    main()

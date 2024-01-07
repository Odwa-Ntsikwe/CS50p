def main():
    greeting = str(input("Greeting: ")).lower().strip()
    output = value(greeting)
    print(f"${output})


def value(greeting):
    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("hello"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()

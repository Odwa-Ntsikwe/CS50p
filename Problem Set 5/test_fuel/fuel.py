def main():
    frac = input("Fraction: ")
    converted_frac = convert(frac)
    print(gauge(converted_frac))


def convert(fraction):
    try:
        x,y = fraction.split("/")
        x = int(x)
        y = int(y)

        if x/y <= 1:
            return int(round((x/y)*100))
        else:
            fraction = input("Fraction: ")
            pass
    except ValueError:
        raise ValueError
    except ZeroDivisionError:
        raise ZeroDivisionError





def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    return f"{percentage}%"


if __name__ == "__main__":
    main()

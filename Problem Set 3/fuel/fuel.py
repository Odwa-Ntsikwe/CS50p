while True:
    try:
        frac = input("Fraction: ")
        x,y = frac.split("/")
        x = int(x)
        y = int(y)
        fuel = round((x/y)*100)
        if x > y:
            frac = input("Fraction: ")

        if fuel <= 1:
            print("E")
        elif fuel > 1 and fuel <= 25:
            print(f"{fuel}%")
        elif fuel > 25 and fuel <= 50:
            print(f"{fuel}%")
        elif fuel > 50 and fuel < 99:
            print(f"{fuel}%")
        else:
            print("F")

    except ValueError:
        pass
    except ZeroDivisionError:
        pass
    else:
        break

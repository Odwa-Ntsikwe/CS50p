groceries = {}

while True:
    try:
        item = input().upper()
        if item in groceries:
            groceries[item] += 1
        else:
            groceries[item] = 1

    except EOFError:
        for key in sorted(groceries.keys()):
            print(groceries[key], key)
        break
    except KeyError:
        pass

def main():
    variable = input("camelCase: ")
    print("snake_case:", convert_case(variable))

def convert_case(string):
    snake_case = ""
    for char in string:
        if char.isupper():
            snake_case += "_" + char.lower()
        else:
            snake_case += char
    return snake_case


main()

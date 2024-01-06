def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    elif len(s) <= 6 and len(s) >= 2 and s[0:2].isalpha() and s.isalnum():
        for i in range(len(s)):
            if s[i].isdigit():
                if  s[i:].isdigit() and s[i] != "0":
                    return True
                else:
                    return False
        return True

    for c in s:
        if c in [".", ",", "!", "?"]:
            return False

    return True


main()

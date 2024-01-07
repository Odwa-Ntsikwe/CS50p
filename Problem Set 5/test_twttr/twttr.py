def main():
    text = input("Input: ")
    output = shorten(text)
    print(f"Output: {output}")


def shorten(word):
    vowels = ["a", "e","i", "o", "u"]
    new_text = ""

    for char in word:
        if char.lower() not in vowels:
            new_text += char
    return new_text



if __name__ == "__main__":
    main()


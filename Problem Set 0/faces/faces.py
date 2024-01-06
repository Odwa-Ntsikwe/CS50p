def main():
    sentence = input("Enter a string: ")
    print(converter(sentence))

def converter(text):
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")

    return text

main()

text = input("Input: ")

vowels = ["a", "e","i", "o", "u"]
new_text = ""

for char in text:
    if char.lower() not in vowels:
        new_text += char
print("Output:", new_text)

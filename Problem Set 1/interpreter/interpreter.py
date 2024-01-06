expression = input("Expression: ")

x, y, z = expression.split(" ")

a = float(x)
b = float(z)

if y == "+":
    answer = a + b
if y == "-":
    answer = a - b
if y == "*":
    answer = a * b
if y == "/":
    answer = a / b

print(round(answer, 1))

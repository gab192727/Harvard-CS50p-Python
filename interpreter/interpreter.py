x, y, z = input("Expression: ").split(" ")
x = float(x)
z = float(z)
result = ""
if y == '+':
    result = x + z
elif y == '-':
    result = x - z
elif y == '*':
    result = x * z
elif y == '/':
    result = x / z

print(round(result, 1))

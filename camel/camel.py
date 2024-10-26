camelcase = input("camelCase: ")
snakecase = ""

for i in camelcase:
    if i.isupper():
        snakecase += "_" + i
    else:
        snakecase += i

print(f"snake_case: {snakecase.lower()}")

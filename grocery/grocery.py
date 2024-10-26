items = {}

try:
    while True:
        item = input("")
        if not item:
            break

        if item in items:
            items[item] += 1

        else:
            items[item] = 1
except ValueError:
    pass
except EOFError:
    for item, count in sorted(items.items()):
        print(f"{count} {item.upper()}")

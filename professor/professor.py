import random


def main():
    level = get_level()
    score = 0
    for i in range(10):
        x, y, z = generate_integer(level)
        tries = 0
        while tries < 3:
            try:
                w = int(input(f"{x} + {y} = "))

                if w == z:
                    score += 1
                    break

                else:
                    print("EEE")
                    tries += 1

            except ValueError:
                continue

        else:
            print(f"{x} + {y} = {z}")

    print(f"Score: {score}")

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            continue


def generate_integer(level):
    x, y = None, None
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    elif level == 3:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
    z = x + y
    return x, y, z


if __name__ == "__main__":
    main()

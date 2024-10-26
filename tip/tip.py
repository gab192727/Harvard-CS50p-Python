

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    x = d.removeprefix('$')
    return float(x)


def percent_to_float(p):
    y = p.removesuffix('%')
    result = float(y) / 100
    return result


main()

def main():
    while True:
        x = input("Fraction: ")
        value = convert(x)
        if value is ZeroDivisionError:
            break
        elif value is ValueError:
            continue
        elif value == "E" or value == 'F':
            print(value)
        else:
            print(value)


def convert(fraction):
    try:
        x, z = fraction.split("/")
        x = int(x)
        z = int(z)
        if z == 0 or x == 0:
            return ZeroDivisionError
        elif x > z:
            return ValueError
        else:
            percent = gauge(round(x / z * 100))
            return percent
    except ValueError:
        return ValueError



def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()

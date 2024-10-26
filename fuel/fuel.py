while True:
    try:
        x, z = input("Fraction: ").split("/")
        if x == "0":
            print("E")
            break
        elif int(x) > int(z):
            continue
        else:
            w = round(int(x) / int(z) * 100)
            if w == 1:
                print("E")
                break
            elif w >= 99:
                print("F")
                break
            else:
                print(f"{w}%")
                break
    except (ValueError, ZeroDivisionError):
        continue















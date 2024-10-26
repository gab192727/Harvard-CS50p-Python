

def main():
    print(validate(input("IPv4 Address: ").strip()))

def validate(ip):
    try:
        check = ip.split('.')
        if len(check) != 4:
            return False
        for i in check:
            if not i.isdigit() or int(i) > 255:
                return False
        return True
    except ValueError:
        return False

if __name__ == "__main__":
    main()


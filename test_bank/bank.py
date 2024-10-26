

def main():
    greet = input('Greeting: ')
    print(f"${value(greet)}")


def value(greetings):
    illegal_word = ("hello", 'Hello')
    greetings = greetings.strip().lower()

    if any(greetings.startswith(word) for word in illegal_word):
        return f"{0}"
    elif greetings[0] == "h":
        return f"{20}"
    else:
        return f"{100}"


if __name__ == '__main__':
    main()

import re

def main():
    print(parse(input("HTML: ")))

def parse(input):
    if parsing := re.search(r'<iframe[^>]+src="https?://(www\.)?youtube\.com/embed/([^"]+)"', input):
        return f'https://youtu.be/{parsing.group(2)}'

    return None


if __name__ == '__main__':
    main()


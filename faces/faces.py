emojis = {
    ':)': "🙂",
    ':(': "🙁"
}
def convert(words):
    converted = ""
    for word in words:
        converted += emojis.get(word, word) + " "
    return converted

def main():
    sentence = input("")
    words = sentence.split(" ")
    result = convert(words)
    print(result)


if __name__ == "__main__":
    main()

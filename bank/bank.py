greet = input('Greeting: ').lstrip()
illegal_word = "hello", 'Hello'
if greet.startswith(illegal_word):
    print("$0")
elif greet[0].lower() == "h":
    print("$20")
else:
    print("$100")

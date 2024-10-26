great_question = ["42", "forty two", "forty-two", "Forty Two", "Forty-Two", "FoRty TwO", ]
answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
if answer.lower().strip() in [ans.lower().strip() for ans in great_question]:
    print("Yes")
else:
    print("No")

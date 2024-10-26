from random import randint

correct_number = randint(1, 10)

while True:
    try:

        level = int(input('Level: '))

        if level > 0:
            correct_number = randint(1, level)
            break

    except ValueError:
        continue

while True:
    try:

        guess = int(input('Guess:'))

        if guess == correct_number:
            print('Just right!')
            break

        elif guess > correct_number:
            print('Too large!')

        elif guess < correct_number:
            print('Too small!')

    except ValueError:
        continue
    
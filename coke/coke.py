amountDue = 50
possibleCoin = [25, 10, 5]

while True:
    print(f"Amount Due: {amountDue}")
    insertCoin = int(input("Insert Coin: "))
    if insertCoin not in possibleCoin:
        continue
    else:
        amountDue -= insertCoin

    if amountDue == 0:
        print("Change Owed: 0")
        break
    elif amountDue < 0:
        print(f"Change Owed: {abs(amountDue)}")
        break

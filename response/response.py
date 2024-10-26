from validators import email

email_address = input("What's your email address? ")

if email(email_address):
    print("Valid")
else:
    print("Invalid")

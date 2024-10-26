def main():
    time = input("What time is it? ")
    hours = convert(time)
    if 7.0 <= hours <= 8.0:
        print("breakfast time")
    elif 12.0 <= hours <= 13.0:
        print("Lunch time")
    elif 18.0 <= hours <= 19.0:
        print("dinner time")

def convert(time):
    hour, minute = time.split(":")
    time = int(hour) + int(minute) / 60
    return time

if __name__ == "__main__":
    main()

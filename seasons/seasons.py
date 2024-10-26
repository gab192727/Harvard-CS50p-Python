from datetime import date, timedelta
import sys
import inflect

p = inflect.engine()

def main():
    try:
        year_input, month_input, day_input = input("Date of Birth: ").split("-")
        year, month, day = int(year_input), int(month_input), int(day_input)
    except ValueError:
        sys.exit("Invalid Date")
    print(convert_to_minutes(year, month, day))


def convert_to_minutes(year, month, day):
    try:
        current_date = date.today()
        difference = current_date - date(year, month, day)
        total_minutes = difference.days * 24 * 60
        minutes_in_words = p.number_to_words(total_minutes, andword='')
        return f"{minutes_in_words} minutes".capitalize()
    except ValueError:
        return "Invalid Date"


if __name__ == "__main__":
    main()


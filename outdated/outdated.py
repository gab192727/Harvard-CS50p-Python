months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    try:

        date = input("Date: ").strip()

        if date[0].isalpha():
            date = date.title()

            if "/" in date or "," not in date:
                continue

            m, d, y = date.split(" ")
            m = int(months.index(m)) + 1
            d = d.replace(",", "")

            if m > 12 or int(d) > 31:
                continue

            else:
                print(f"{y}-{str(m).zfill(2)}-{str(d).zfill(2)}")
                break

        elif date[0].isalnum():
            m, d, y = date.split("/")

            if not (d or y).isalnum() or int(m) > 12 or int(d) > 31:
                continue


            else:
                print(f"{y}-{str(m).zfill(2)}-{str(d).zfill(2)}")
                break

    except ValueError:
        continue

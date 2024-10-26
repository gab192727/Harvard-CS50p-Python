import re


def main():
    print(convert(input("Hours: ").strip()))


def convert(input_str):

    if matches := re.search(r"([0-9]{1,2})(:([0-9]{2}))? (AM|PM) to ([0-9]{1,2})(:([0-9]{2}))? (AM|PM)", input_str):
        start_hour = int(matches.group(1))
        start_minute = int(matches.group(3) or 0)
        end_hour = int(matches.group(5))
        end_minute = int(matches.group(7) or 0)
        if start_hour <= 12 and end_hour <= 12 and start_minute <= 59 and end_minute <= 59:
            if matches.group(4) == "PM":
                start_hour += 12
                if matches.group(8) == "PM":
                    end_hour += 12
            elif matches.group(4) == "AM":
                if matches.group(8) == "PM":
                    end_hour += 12
                    if start_hour == 12:
                        start_hour = 0
                        if end_hour == 24:
                            end_hour = 12
            else:
                raise ValueError

        else:
            raise ValueError

        return f"{start_hour:02}:{start_minute:02} to {end_hour:02}:{end_minute:02}"
    else:
        raise ValueError



if __name__ == "__main__":
    main()

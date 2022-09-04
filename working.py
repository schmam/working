# program to convert time frame (e.g., "9:00 AM to 5:00 PM" or "9 AM to 5 PM") to a 24-hour format (e.g., "13:00", "23:00")

import re       # needed for re.search
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):

# first format to look for is, e.g., "9:00 AM to 5:00 PM" (second format will appear later in the function)

    if match := re.search(r"(1?[0-9]+):([0-9]+[0-9]+) ([A-Z]+M) to (1?[0-9]+):([0-9]+[0-9]+) ([A-Z]+M)", s, re.IGNORECASE):

        # checks minutes and hours for validity, returns ValueError if hours or minutes are not within valid range

        if int(match.group(1)) > 12:
            return ValueError
        if int(match.group(2)) > 59:
            return ValueError
        if int(match.group(4)) > 12:
            return ValueError
        if int(match.group(5)) > 59:
            return ValueError

        if match.group(3) == "AM":                  # if time in first position is AM, no need to add 12 hours
            if match.group(1) == "12":              # if 12:00 AM, return "00:00"
                hour_1 = 0
            else:
                hour_1 = int(match.group(1))
            minute_1 = int(match.group(2))

        elif match.group(3) == "PM":                # add 12 hours if PM
            if match.group(1) == "12":              # if 12:00 AM, return "12:00"
                hour_1 = 12
            else:
                hour_1 = (12 + int(match.group(1)))
            minute_1 = int(match.group(2))
        else:
            return ValueError

        if match.group(6) == "AM":                  # if time in first position is AM, no need to add 12 hours
            if match.group(4) == "12":              # if 12:00 AM, return "00:00"
                hour_2 = 0
            else:
                hour_2 = int(match.group(4))
            minute_2 = int(match.group(5))

        elif match.group(6) == "PM":                # add 12 hours if PM
            if match.group(4) == "12":              # if 12:00 AM, return "12:00"
                hour_2 = 12
            else:
                hour_2 = (12 + int(match.group(4)))
            minute_2 = int(match.group(5))
        else:
            return ValueError

        return f"{hour_1:02}:{minute_1:02} to {hour_2:02}:{minute_2:02}"

# second format to look for is, e.g., "9 AM to 5 PM"

    elif match := re.search(r"([0-9]?[0-9]+) ([A-Z]+M) to ([0-9]?[0-9]+) ([A-Z]+M)", s, re.IGNORECASE):

        if int(match.group(1)) > 12:
            return ValueError
        if int(match.group(3)) > 12:
            return ValueError

        if match.group(2) == "AM":                  # if time in first position is AM, no need to add 12 hours
            if match.group(1) == "12":              # if 12:00 AM, return "00:00"
                hour_1 = 0
            else:
                hour_1 = int(match.group(1))
        elif match.group(2) == "PM":                # add 12 hours if PM
            if match.group(1) == "12":              # if 12:00 AM, return "12:00"
                hour_1 = 12
            else:
                hour_1 = (12 + int(match.group(1)))
        else:
            return ValueError

        if match.group(4) == "AM":                  # if time in first position is AM, no need to add 12 hours
            if match.group(3) == "12":              # if 12:00 AM, return "00:00"
                hour_2 = 0
            else:
                hour_2 = int(match.group(3))
        elif match.group(4) == "PM":                # add 12 hours if PM
            if match.group(3) == "12":              # if 12:00 AM, return "12:00"
                hour_2 = 12
            else:
                hour_2 = (12 + int(match.group(3)))
        else:
            return ValueError

        return f"{hour_1:02}:00 to {hour_2:02}:00"


    else:
        return ValueError



if __name__ == "__main__":
    main()

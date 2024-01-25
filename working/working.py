import random
import re
import sys


def main():
    print(convert(input("Hours: ")))
    sys.exit(0)


def convert(s):
    time = s.strip()
    if m := re.fullmatch(
        r"^(?:(?P<hr1>[1-9]|1[0-2]):?(?P<min1>[0-5][0-9])?) (?P<tag1>AM|PM) to (?:(?P<hr2>[1-9]|1[0-2]):?(?P<min2>[0-5][0-9])?) (?P<tag2>AM|PM)$",
        time,
        re.I,
    ):
        g = m.groupdict(default="00")
        #print(g)
        h1, m1, t1 = int(g["hr1"]), int(g["min1"]), g["tag1"]
        h2, m2, t2 = int(g["hr2"]), int(g["min2"]), g["tag2"]
        return f"{get_time_in_24_hr(h1,m1,t1)} to {get_time_in_24_hr(h2,m2,t2)}"
    else:
        raise ValueError(f"Invalid time format: {s}")


def get_time_in_24_hr(h, m, t):
    if isinstance(h,int) and isinstance(m,int) and isinstance(t,str):
        match t.upper():
            case "AM" if h == 12:
                return f"00:{m:02}"
            case "AM":
                return f"{h:02}:{m:02}"
            case "PM" if h == 12:
                return f"{12}:{m:02}"
            case "PM":
                hr = (int(h) + 12) % 24
                return f"{hr:02}:{m:02}"
    else:
        raise ValueError(f"Invalid parameter. check if: h(int) | m(int) | t(str)") 
    
        


if __name__ == "__main__":
    main()
    # print(get_time_in_24_hr("12",30,"AM"))


# h1= "9 AM to 5 PM"
# h2= "9:00 AM to 5:00 PM"
# h3 = "11:00 AM to 12:00 PM"
# h4 = "9:00 AM to 17:00 PM"


# print(get_time_in_24_hr("12","00","AM"))
# print(get_time_in_24_hr("12","23","AM"))
# print(get_time_in_24_hr("1","23","AM"))
# print(get_time_in_24_hr("12","00","PM"))
# print(get_time_in_24_hr("1","00","PM"))
# print(get_time_in_24_hr("7","59","PM"))
# print(get_time_in_24_hr("11","30","PM"))

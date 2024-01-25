import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):  # validate ip is an IPv4 address
    pattern = re.compile(
        r"^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$"
    )
    pattern2 = re.compile(
        r"^(([0-9])((?<!0)[0-9])?((?<=1\d)\d|(?<=2[0-4])\d|(?<=25)[0-5])?\.){3}(([0-9])((?<!0)[0-9])?((?<=1\d)\d|(?<=2[0-4])\d|(?<=25)[0-5])?)$"
    )
    return True if (pattern.match(ip) and pattern2.match(ip)) else False if pattern2.match(ip) else False


if __name__ == "__main__":
    main()

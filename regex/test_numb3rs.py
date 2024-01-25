import random

from numb3rs import validate


def gen_same_ndigit_IPv4_in_range(n):
    if n in [1, 2, 3]:
        ip = []
        range_ = range(4)
        match n:
            case 1:
                for _ in range_:
                    d = random.randint(0, 9)
                    ip.append(str(d))
                ip = ".".join(ip)
                return ip

            case 2:
                for _ in range_:
                    d = random.randint(10, 99)
                    ip.append(str(d))
                ip = ".".join(ip)
                return ip

            case 3:
                for _ in range_:
                    d = random.randint(100, 255)
                    ip.append(str(d))
                ip = ".".join(ip)
                return ip


def gen_diff_digit_IPv4_in_range():
    ip = []
    for _ in range(4):
        d = random.randint(0, 255)
        ip.append(str(d))
    ip = ".".join(ip)
    return ip


def gen_invalid_IPv4():
    ip = []
    n = random.randint(1, 4)
    rem = 4 - n
    for _ in range(n):
        invalid_range = random.randint(256, 1000)
        ip.append(str(invalid_range))
    if rem:
        for _ in range(rem):
            valid_range = random.randint(0, 255)
            ip.append(str(valid_range))

    ip = ".".join(ip)
    return ip


def test_digit_IPv4_in_range():
    for _ in range(10):
        assert validate(gen_same_ndigit_IPv4_in_range(1)) == True


def test_tens_IPv4_in_range():
    for _ in range(10):
        assert validate(gen_same_ndigit_IPv4_in_range(2)) == True


def test_hundreds_IPv4_in_range():
    for _ in range(10):
        assert validate(gen_same_ndigit_IPv4_in_range(3)) == True


def test_diff_digit_IPv4_in_range():
    for _ in range(10):
        assert validate(gen_diff_digit_IPv4_in_range()) == True


def test_invalid_IPv4():
    for _ in range(10):
        assert validate(gen_invalid_IPv4()) == False


if __name__ == "__main__":
    n = random.randint(1, 3)
    print("\nValid IPv4:")
    print(gen_same_ndigit_IPv4_in_range(n))
    for _ in range(10):
        print(gen_diff_digit_IPv4_in_range())

    print("\nInvalid IPv4:")
    for _ in range(10):
        print(gen_invalid_IPv4())

    
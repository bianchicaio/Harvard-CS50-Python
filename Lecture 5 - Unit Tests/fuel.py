import sys

def main():
    user_fraction = input("Fraction: ")
    print(gauge(convert(user_fraction)))

def convert(fraction):
    x, y = fraction.split("/")
    if int(y) == 0:
        return ZeroDivisionError
    elif int(x) > int(y):
        return ValueError
    else:
        return int(int(x) / int(y) * 100)

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
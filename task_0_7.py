def convert_to__celciius(fahrenheit):
    celcius = (fahrenheit - 32) * (5 / 9)
    return round(celcius, 2)


def convert_to_fahrenheit(celcius):
    fahrenheit = (celcius * (9 / 5)) + 32
    return round(fahrenheit, 2)


def main():
    print(convert_to__celciius(92))
    print(convert_to_fahrenheit(33))


if __name__ in "__main__":
    main()

def find_biggest_num2(*args):
    maximum_number = args[0]
    for number in args:
        if number > maximum_number:
            maximum_number = number
    return maximum_number


def main():
    print(find_biggest_num2(-1, -11, -3, -9, -5, -6))


if __name__ in "__main__":
    main()

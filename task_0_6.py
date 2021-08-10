def find_biggest_num2(*args):
    maximum_number = 0

    for number in args:
        if number > maximum_number:
            maximum_number = number

    return maximum_number


def main():
    print(find_biggest_num2(1, 2, 3, 9, 5, 6))


if __name__ in "__main__":
    main()

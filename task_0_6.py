def find_biggest_num2(*args):
    numbers_list = []
    for number in args:
        numbers_list.append(number)

    maximum_number = numbers_list[0]

    for number in numbers_list:
        if number > maximum_number:
            maximum_number = number
    return maximum_number


def main():
    print(find_biggest_num2(-1, -11, -3, -9, -5, -6))


if __name__ in "__main__":
    main()

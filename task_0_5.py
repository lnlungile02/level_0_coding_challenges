def triangle_area_calc(side_a, side_b, side_c):

    semi_parameter = (side_a + side_b + side_c) / 2
    area = (
        semi_parameter
        * (semi_parameter - side_a)
        * (semi_parameter - side_b)
        * (semi_parameter - side_c)
    ) ** 0.5

    return round(area, 2)


def main():
    print(triangle_area_calc(float(4), float(6), float(8)))


if __name__ in "__main__":
    main()

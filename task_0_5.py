def triangle_area_calc(side_a,side_b,side_c):
    
    semi = (side_a + side_b + side_c)/2
    area = (semi* (semi - side_a)* (semi - side_b)* (semi - side_c))**0.5

    return str(round(area,2))


print(triangle_area_calc(float(4),float(6),float(8)))

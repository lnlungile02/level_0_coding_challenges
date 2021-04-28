def find_biggest_num2(*args):
    
    biggest_number=0
    for x in args:
        if x >biggest_number:
            biggest_number=x

    
    return biggest_number


print(find_biggest_num2(1,2,3,4,5,6))

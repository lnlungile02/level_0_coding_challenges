def find_biggest_num(num1,num2,num3):
    
    biggest_number=0
    if num1>num2 and num1>num3:
        biggest_number=num1
    elif num2>num1 and num2>num3:
        biggest_number=num2
    else :
        biggest_number=num3
    
    print(biggest_number)

find_biggest_num(15,4,1)
    
#updated function

def find_biggest_num2(*args):
    
    biggest_number=0
    for x in args:
        if x >biggest_number:
            biggest_number=x

    
    print(biggest_number)


find_biggest_num2(1,2,3,4,5,6,7,8)

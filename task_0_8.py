def convert_to_time(number):
    hours = number//60
    minutes=number%60

    print(str(hours) + " " +"hours and" + " " + str(minutes)+ " " + "minutes")

convert_to_time(133)

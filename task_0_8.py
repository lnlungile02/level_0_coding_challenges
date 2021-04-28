def convert_to_time(number):

  if number < 60:
    return "0:" + str(number)
  else:
    number = number % (24*3600)
    hours = number // 60
    number %= 60
    return str(hours) + ":" + str(number)
 
print(convert_to_time(11))

def convert_to_time(number):

  if number < 60:
    return "0 " +"hours,"+ str(number) + " minutes"
  else:
    number = number % (24*3600)
    hours = number // 60
    number %= 60
    return str(hours) +  " hours, " + str(number) + " minutes"
 
print(convert_to_time(11))

def convert_to_time(number):

  if number < 60:
    print ("0:" + str(number))
  else:
    number = number % (24*3600)
    hours = number // 60
    number %= 60
    print (str(hours) + ":" + str(number))
 
convert_to_time(126)

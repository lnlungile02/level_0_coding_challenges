def convert_to__celciius(f):
    celcius=(f-32)*(5/9)
    return celcius

def convert_to_fahrenheit(c):
    fahrenheit = (c*(9/5))+32
    return fahrenheit

print(convert_to__celciius(92))

print(convert_to_fahrenheit(33))

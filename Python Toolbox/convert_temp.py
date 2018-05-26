temp = 25
def convert_temp(x):
     """Converts the temparature from Celsius to Fahrenheit"""
     global temp
     temp = (x * 1.8) + 32
convert_temp(temp)
print(temp)

output: 77.0

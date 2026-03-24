# Exercise 2 - Temperature Conversion

def convert_to_fahrenheit(degrees_celsius):
    return degrees_celsius * (9 / 5) + 32


def convert_to_celsius(degrees_fahrenheit):
    return (degrees_fahrenheit - 32) * (5 / 9)


assert convert_to_fahrenheit(0) == 32
assert convert_to_fahrenheit(100) == 212
assert convert_to_celsius(0) == -17.77777777777778
assert convert_to_celsius(180) == 82.22222222222223
assert convert_to_celsius(convert_to_fahrenheit(15)) == 15
# Rounding errors cause a slight discrepancy:
assert convert_to_celsius(convert_to_fahrenheit(42)) == 42.00000000000001

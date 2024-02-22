# Define a function that converts Fahrenheit to Celsius.
def to_celsius(x):
     return (x-32) * 5/9

# Create a table of Celsius-->Fahrenheit conversions every 10 degrees, 0-100
for x in range(0, 101, 10):
     print(x, to_celsius(x))
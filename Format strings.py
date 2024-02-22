# Use format() method to insert values into your string, indicated by braces.
name = 'Manuel'
number = 3
print('Hello {}, your lucky number is {}.'.format(name, number))

# You can assign names to designate how you want values to be inserted.
name = 'Manuel'
number = 3
print('Hello {name}, your lucky number is {num}.'.format(num=number, name=name))

# You can use argument indices to designate how you want values to be inserted.
print('Hello {1}, your lucky number is {0}.'.format(number, name))

# Example inserting prices into string
price = 7.75
with_tax = price * 1.07
print('Base price: ${} USD. \nWith tax: ${} USD.'.format(price, with_tax))

# Use :.2f to round a float value to two places beyond the decimal.
print('Base price: ${:.2f} USD. \nWith tax: ${:.2f} USD.'.format(price, with_tax))

# Define a function that converts Fahrenheit to Celsius.
def to_celsius(x):
    return (x-32) * 5/9

# Create a temperature conversion table using string formatting
for x in range(0, 101, 10):
    print("{:>3} F | {:>6.2f} C".format(x, to_celsius(x)))
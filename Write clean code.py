# This code does the same thing for two different people.
name = "Marisol"
number = len(name)*9
print("Hello " + name + ". Your lucky number is " + str(number))

name = "Ardashir"
number = len(name)*9
print("Hello " + name + ". Your lucky number is " + str(number))
################
# Define a function that simplifies the above code and makes it reusable.
def lucky_number(name):
    number = len(name)*9
    print("Hello " + name + ". Your lucky number is " + str(number))

lucky_number("Marisol")
lucky_number("Ardashir")
#############
# This code requests a number from the user and returns its factorial,
# printing each iteration of the multiplication.
a = input(); y = 1

for i in range(int(a)):
    y = y*(i+1)
    print(y)
################
# This function takes an integer as an input and returns its factorial.
def factorial(n):
    # Exclude 0 as product, start with 1
    y = 1
    for i in range(int(n)):
        y = y*(i+1)
    return y

# Enter a numerical value between 1-9 in the command line that appears.
input_num = input()
# Apply factorial function to an integer input
print(factorial(input_num))


# The print() function can print text to the screen.
print('Black dove, where will you go?')
########################################## The type() function returns an object's data type.
number = 15
print(type(number))
##########################################
# The str() function converts an object into a string.
number = str(number)
print(type(number))
######
# Define a function.
def greeting(name):

    print('Welcome, ' + name + '!')
    print('You are part of the team!')

greeting('Rebecca')
##############
# Define a function to calculate the area of a triangle.
def area_triangle(base, height):
    return base * height / 2
# Use the function to assign new variables and perform calculations.
area_a = area_triangle(5, 4)
area_b = area_triangle(7, 3)
total_area = area_a + area_b
print(total_area)
#################
# Define a function that converts hours, minutes, and seconds to total seconds.
def get_seconds(hours, minutes, seconds):
    total_seconds = 3600*hours + 60*minutes + seconds
    return total_seconds
# Use the function to return a result.
print(get_seconds(16, 45, 20))


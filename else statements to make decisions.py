# Define a function that checks validity of username based on length.
def hint_username(username):
    if len(username) < 8:
        print("Invalid username. Must be at least 8 characters long.")
    else:
        print("Valid username.")

# Define a function that uses modulo to check if a number is even.
def is_even(number):
    if number % 2 == 0:
        return True
    return False

print(is_even(19))
###########################
# Define a function that checks validity of username based on length.
def hint_username(username):
    if len(username) < 8:
        print("Invalid username. Must be at least 8 characters long.")
    elif len(username) > 15:
        print("Invalid username. Cannot exceed 15 characters.")
    else:
        print("Valid username.")

print(hint_username("ljñkljfñklasdjflkñadjglk{a"))
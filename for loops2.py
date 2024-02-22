# Example of reading in a .txt file line by line with a for loop
with open('zen_of_python.txt') as f:
    for line in f:
        print(line)
print('\nI\'m done.')
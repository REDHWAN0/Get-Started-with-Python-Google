# This list comprehension adds 10 to each number in the list:

numbers = [1, 2, 3, 4, 5]
new_list = [x + 10 for x in numbers]
print(new_list)

print('\n')
""" This next list comprehension extracts the first and last letter of each word as a tuple, 
but only if the word is more than five letters long.
"""
words = ['Emotan', 'Amina', 'Ibeno', 'Sankwala']
new_list = [(word[0], word[-1]) for word in words if len(word) > 5]
print(new_list)
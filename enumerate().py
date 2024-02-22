#  iterate over a sequence while keeping track of each element’s index.

letters = ['a', 'b', 'c']
for index, letter in enumerate(letters):
   print(index, letter)

print('\n')

letters = ['a', 'b', 'c']
for index, letter in enumerate(letters, 2):
   print(index, letter)
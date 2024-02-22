# change an individual item in a list by specifying its index and assigning a new value to it. For example:
my_list = ['Macduff', 'Malcolm', 'Duncan', 'Banquo']
my_list[2] = 'Macbeth'
print(my_list)
#=================================
print('\n')
#  insert in place of the indicated slice:
my_list = ['Macduff', 'Malcolm', 'Macbeth', 'Banquo']
my_list[1:3] = [1, 2, 3, 4]
print(my_list)

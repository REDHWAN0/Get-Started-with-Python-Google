""" There are two main ways to create lists in Python:
Square brackets: []
The list function: list()
When instantiating a list using brackets, separate each element with a comma.
For example, the following code creates a list of strings:
"""
list_a = ['olive', 'palm', 'coconut']
print(list_a)
#=================================
print('\n')
# You can also create a list of integers:
list_b = [8, 6, 7, 5, 3, 0, 8]
print(list_b)
#=================================
print('\n')
# Or a list of mixed data types:
list_c = ['Abidjan', 14.2, [1, 2, None], 'Zagreb']
print(list_c)
#=================================
print('\n')
# To create an empty list, use empty brackets or the list() function:
empty_list_1 = []
empty_list_2 = list()
print(empty_list_2)
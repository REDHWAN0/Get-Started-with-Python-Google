""" The first element of a list has index zero,
 the second element has index one, and so on. Use square brackets to index:
"""
phrase = ['Astra', 'inclinant', 'sed', 'non', 'obligant']
print(phrase[1])
#=================================
print('\n')
# use negative indices to access items from the end of a list:
phrase = ['Astra', 'inclinant', 'sed', 'non', 'obligant']
print(phrase[-1])
#=================================
print('\n')
""" Use slicing to extract a sublist. To slice, 
use square brackets containing a range of indices separated by a colon:
"""
phrase = ['Astra', 'inclinant', 'sed', 'non', 'obligant']
print(phrase[1:4])
#=================================
print('\n')
""" this code returned a sublist containing the elements 
at indices one, two, and three of phrase. 
The ending index of the slice is not included.
"""
phrase = ['Astra', 'inclinant', 'sed', 'non', 'obligant']
print(phrase[:3])
print(phrase[3:])

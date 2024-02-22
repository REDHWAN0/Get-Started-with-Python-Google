""" The zip() function is a built-in Python function
that does what the name implies: It performs an element-wise combination of sequences.
"""

cities = ['Paris', 'Lagos', 'Mumbai']
countries = ['France', 'Nigeria', 'India']
places = zip(cities, countries)

print(places)
print(list(places))

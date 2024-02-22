import re

my_string = 'Three sad tigers swallowed wheat in a wheat field'

print(re.search('wall', my_string))
print('\n')
print(re.search('[bms]ad', my_string))
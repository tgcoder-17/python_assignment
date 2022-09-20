import re
text = input("Enter a string: ")
patterns = '^a(b*)$'
if re.search(patterns, text):
    print('Found a match!')
else:
    print('Not matched!')

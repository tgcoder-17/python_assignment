import re
patterns = '^[a-z]+_[a-z]+$'
text=input("Enter a string: ")
if re.search(patterns, text):
    print('Found a match!')
else:
    print('Not matched!')
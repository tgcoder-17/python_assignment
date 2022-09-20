import re
reg = r'[^a-zA-Z0-9]'
s = input("Enter String: ")
pat = re.compile(reg)
mat = re.search(pat, s)
if not mat:
    print("Valid String")
else:
    print("Invalid String")
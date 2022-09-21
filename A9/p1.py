import re

ex = re.compile(r"[0-9]")

st = input("Enter word file name:").split(".")[0]

valid = ex.search(st)

if valid:
    print("Invalid Filename")
else:
    print("Valid Filename")

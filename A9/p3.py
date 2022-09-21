import re

myRule =  re.compile(r"[^ ]+\.py")
st = "This contains two files, hw3.py and uppercase.py"

match = myRule.search(st)

print(match.group())

allMatch = myRule.findall(st)
print(allMatch)
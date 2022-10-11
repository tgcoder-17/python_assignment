import re

ex = re.compile(r'@msubaroda.ac.in$')

path = "G:/MSU/Sem-7/Python/Programs/A9/temp/emails.txt"

li = []

with open(path, "r" ) as file:
    for line in file.readlines():
        print(line)
        valid = ex.search(line)
        if valid:
            li.append(line.removesuffix("@msubaroda.ac.in\n"))


print(li)



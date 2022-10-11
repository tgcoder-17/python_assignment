import re
import os

ex = re.compile(r'def +')

dir = "G:/MSU/Sem-7/Python/Programs/A9/temp"

dir_list = os.listdir(dir)

li = []

for fileName in dir_list:
    with open(dir+"/"+fileName, "r") as file:
        for line in file.readlines():
            valid = ex.search(line)
            if valid:
                li.append(
                    (line.split("def ")[1].removesuffix("():\n"), fileName))

li.sort(key= lambda x: x[0])
print(li)

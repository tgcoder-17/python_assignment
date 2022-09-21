import re

ex = re.compile(r"[0-9]")
li = []

while True:
    st = input("Enter word file name[X for Exit]:").split(".")[0]
    if st.lower() == "x":
        break

    notValid = ex.search(st)

    if not notValid:
        li.append(st)

print(li)
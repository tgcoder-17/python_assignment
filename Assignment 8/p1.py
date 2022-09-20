import re
import os
import glob
directory = "G:\MSU\Sem-7\Python\Programs\Assignment 8"
print ("All files in ",directory)
for filename in os.listdir(directory):
    print(filename)
print("\n\nFiles that contain file1.log in thair name....\n")

print("1. Using re module... ")
for filename in os.listdir(directory):
    x = re.search("^file1.log", filename)
    if x:
        print(filename)

files = glob.glob(directory + '/file1.log*')
print("\n2. Using glob...")
for f in files:
    print(f)
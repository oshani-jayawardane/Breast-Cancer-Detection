import os

# specify the path of the folder you want to search
path = "enter/path"

# use list comprehension to get a list of all subfolder names
subfolders = [f.name for f in os.scandir(path) if f.is_dir()]

# convert the list to a string with new line character
subfolders_str = '\n'.join(subfolders)

# print the string with subfolder names and new line characters
print(subfolders_str)

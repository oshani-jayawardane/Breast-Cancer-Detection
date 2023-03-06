# delete other files inside a (one) directory that are not PNG

import os

dir_path = r"enter/file/name/here"

for filename in os.listdir(dir_path):
    if not filename.endswith(".png"):
        os.remove(os.path.join(dir_path, filename))

#ouput
print("Files except for PNG successfully deleted")
# delete other files inside all subdirectories inside a directory that are not PNG

import os

dir_path = r"enter/path/to/main/directory"

# loop through all directories and subdirectories
for root, dirs, files in os.walk(dir_path):
    # loop through all files in each directory
    for file in files:
        # check if file does not end with .png extension
        if not file.endswith(".png"):
            # remove the file
            os.remove(os.path.join(root, file))
            
print("Successfully deleted all files except for PNG")

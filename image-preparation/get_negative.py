# get negative of images in all sub directories

import os
import numpy as np
from PIL import Image

dir_path = "C:/Users/Asus/Desktop/FYP/_WORK/images/negative"

for root, dirs, files in os.walk(dir_path):
    for file in files:
        if file.lower().endswith(('.png', '.jpg', '.jpeg')):
            # Load the image
            image_path = os.path.join(root, file)
            image = Image.open(image_path)
            # Convert to negative
            image_arr = np.array(image)
            neg_image_arr = 255 - image_arr
            neg_image = Image.fromarray(neg_image_arr)
            # Save the negative image
            neg_image_path = os.path.splitext(image_path)[0] + "_neg.png"
            neg_image.save(neg_image_path)
            # Delete the previous image
            os.remove(image_path)

print("Successfully converted images to negative in directory:", dirname)
            

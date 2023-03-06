# convert one image from DICOM to PNG and save inside the same directory

import os
import pydicom
from PIL import Image

input_dir = r"emter/path/to/image/here"

# Loop through all files in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith(".dcm"):
        # Read the DICOM file
        dicom_file = pydicom.dcmread(os.path.join(input_dir, filename))

        # Convert the DICOM image to a PIL Image object
        image = Image.fromarray(dicom_file.pixel_array)

        # Save the image as a PNG file in the same directory as the input DICOM file
        output_filename = os.path.splitext(os.path.join(input_dir, filename))[0] + ".png"
        image.save(output_filename)

#output
print("Image converted to PNG file from DICOM")
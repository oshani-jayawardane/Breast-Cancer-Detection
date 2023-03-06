# convert DICOM files in all subdirectories in a folder to PNG and save inside the same sub-directories

import os
import pydicom
from PIL import Image

# function to convert pydicom dataset to PIL Image object
def pydicom_to_pil(dicom_dataset):
    """
    Convert a DICOM dataset to a PIL Image object.

    Args:
        dicom_dataset: The DICOM dataset to convert.

    Returns:
        A PIL Image object.
    """
    # normalize pixel data
    pixel_array = dicom_dataset.pixel_array
    pixel_array = (pixel_array - pixel_array.min()) / (pixel_array.max() - pixel_array.min()) * 255
    pixel_array = pixel_array.astype('uint8')

    # create PIL Image object
    image = Image.fromarray(pixel_array)

    return image

# set directory path where DICOM images are stored
dirname = "Enter/the/path/to/your/folder/here"

# loop through all subdirectories
for root, dirs, files in os.walk(dirname):
    # create a list of DICOM image paths by filtering for files with .dcm extension
    dicom_paths = [os.path.join(root, f) for f in files if os.path.splitext(f)[1] == '.dcm']

    # loop through DICOM image paths
    for dicom_path in dicom_paths:
        # read DICOM file
        dicom_dataset = pydicom.dcmread(dicom_path)
        # convert to PIL Image object
        image = pydicom_to_pil(dicom_dataset)
        # save as PNG file in the same directory with the same name
        output_path = os.path.splitext(dicom_path)[0] + ".png"
        image.save(output_path)

# output
print("Successfully converted DICOM files to PNG format in directory:", dirname)

import os
import filetype
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



directory = r'enter/path'

for filename in os.listdir(directory):
    filepath = os.path.join(directory, filename)

    # try:
    #     os.remove(os.path.splitext(filepath)[0] + '.png')
    #     print("deleted {filename}")
    # except:
    #     print("file {filename} not available")

    # Use the filetype module to identify the type of the file
    kind = filetype.guess(filepath)
    print(kind.extension)

    if kind is None:
        print(f'Skipping unknown file type {filename}.')
        continue

    # Convert JPEG, BMP, and GIF files to PNG format using PIL
    if kind.extension == 'dcm':
        try:
            # Read the DICOM file using pydicom
            dicom = pydicom.dcmread(filepath)
            # convert to PIL Image object
            image = pydicom_to_pil(dicom)
            # Save the image as a PNG file
            png_path = os.path.splitext(filepath)[0] + '.png'
            image.save(png_path, 'PNG')
            print(f'Converted {filename} to PNG format.')
        except:
            print(f'Unable to convert {filename} to PNG format.')
    else:
        print(f'Skipping non-image file {filename}.')

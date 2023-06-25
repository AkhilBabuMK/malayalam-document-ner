import pytesseract as pt
from PIL import Image

import io
pt.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'
def readData(image_bytes: bytes):
    """
    The image is read as bytes and pass to pytesseracts for 
    extracting text 
    
    args:
        - image_bytes (bytes) : incoming images represented as bytes

    """

    img = Image.open(io.BytesIO(image_bytes))
    print(pt.image_to_string(img,lang='mal'))




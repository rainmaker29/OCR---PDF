try :
    from PIL import Image

except ImportError:
    import Image

import pytesseract as pyt

print(pyt.image_to_string(Image.open('img1.png')))

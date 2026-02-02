import pytesseract
from PIL import Image

def text_creation(image_path):
    # loading the image that the user uploaded
    image = Image.open(image_path)
    
    # performing tesseract ocr
    extracted_text = pytesseract.image_to_string(image, lang='eng')
    
    print('Text output:')
    print(extracted_text)
    
if __name__ == '__main__':
    text_creation()
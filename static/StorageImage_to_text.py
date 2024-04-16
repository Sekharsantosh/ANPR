import pytesseract
from PIL import Image

# Path to Tesseract executable (change this if necessary)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text_from_image(image_path):
    # Open the image file
    with Image.open(image_path) as img:
        # Use pytesseract to do OCR on the image
        text = pytesseract.image_to_string(img)
        return text

# Example usage
image_path = 'example_image.png'  # Path to your image file
text = extract_text_from_image(image_path)
print("Extracted Text:")
print(text)

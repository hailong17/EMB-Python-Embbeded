from core import config  # Tự động cấu hình pytesseract khi import
from PIL import Image
import pytesseract

class OCREngine:
    def __init__(self, lang='eng+jpn'):
        self.lang = lang

    def extract_text(self, image: Image.Image) -> str:
        return pytesseract.image_to_string(image, lang=self.lang)

class OCREngine:
    def __init__(self, lang='eng+jpn'):
        self.lang = lang

    def extract_text(self, image: Image.Image) -> str:
        return pytesseract.image_to_string(image, lang=self.lang)

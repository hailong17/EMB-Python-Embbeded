from googletrans import Translator

class TextTranslator:
    def __init__(self):
        self.translator = Translator()

    def translate_text(self, text: str, dest_lang='en') -> str:
        if not text.strip():
            return "No text to translate."
        try:
            translated = self.translator.translate(text, dest=dest_lang)
            return translated.text
        except Exception as e:
            return f"Translation failed: {e}"

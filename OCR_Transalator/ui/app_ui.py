from tkinter import *
from PIL import ImageTk
from core.image_handler import ImageHandler
from core.ocr_engine import OCREngine
from core.translator import TextTranslator

class OCRTranslatorUI:
    def __init__(self, root):
        self.root = root
        self.root.title("OCR Translator App")

        self.image_handler = ImageHandler()
        self.ocr_engine = OCREngine()
        self.translator = TextTranslator()
        self.text = ""

        self._init_widgets()

    def _init_widgets(self):
        self.canvas = Canvas(self.root, width=400, height=300, bg="gray")
        self.canvas.pack()

        btn_frame = Frame(self.root)
        btn_frame.pack()

        Button(btn_frame, text="📷 Capture", command=self._on_capture).grid(row=0, column=0, padx=5)
        Button(btn_frame, text="📂 Upload", command=self._on_upload).grid(row=0, column=1, padx=5)
        Button(btn_frame, text="🔍 Extract", command=self._on_extract).grid(row=0, column=2, padx=5)
        Button(btn_frame, text="🇬🇧 EN", command=lambda: self._on_translate("en")).grid(row=0, column=3, padx=5)
        Button(btn_frame, text="🇯🇵 JA", command=lambda: self._on_translate("ja")).grid(row=0, column=4, padx=5)

        self.textbox = Text(self.root, height=10, width=80)
        self.textbox.pack()

    def _update_canvas(self, img_path):
        img = ImageTk.PhotoImage(file=img_path)
        self.canvas.create_image(0, 0, anchor=NW, image=img)
        self.canvas.image = img

    def _on_upload(self):
        path = self.image_handler.load_image()
        if path:
            self._update_canvas(path)

    def _on_capture(self):
        path = self.image_handler.capture_image()
        if path:
            self._update_canvas(path)

    def _on_extract(self):
        pil_img = self.image_handler.get_pil_image()
        if pil_img:
            self.text = self.ocr_engine.extract_text(pil_img)
            self._display_text(self.text)

    def _on_translate(self, lang):
        text_to_translate = self.textbox.get("1.0", END).strip()
        print("[DEBUG] Original Text:", repr(text_to_translate))  # Debug

        if not text_to_translate:
            self._display_text("⚠️ No text to translate.")
            return

        translated = self.translator.translate_text(text_to_translate, lang)
        print("[DEBUG] Translated Text:", repr(translated))  # Debug

        self._display_text(translated)



    def _display_text(self, text):
        self.textbox.delete("1.0", END)
        self.textbox.insert(END, text)

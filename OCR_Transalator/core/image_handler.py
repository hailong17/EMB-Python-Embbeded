import cv2
from tkinter import filedialog
from PIL import Image
from core.base_image_handler import BaseImageHandler

class ImageHandler(BaseImageHandler):
    def load_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.jpeg *.png")])
        if file_path:
            self.image_path = file_path
        return self.image_path

    def capture_image(self):
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        if ret:
            self.image_path = "assets/captured.jpg"
            cv2.imwrite(self.image_path, frame)
        cap.release()
        return self.image_path

    def get_pil_image(self):
        return Image.open(self.image_path) if self.image_path else None

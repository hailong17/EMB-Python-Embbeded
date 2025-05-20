from tkinter import Tk
from ui.app_ui import OCRTranslatorUI

if __name__ == "__main__":
    root = Tk()
    app = OCRTranslatorUI(root)
    root.mainloop()

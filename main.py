from uart_gui import UARTGUI
import tkinter as tk

def main():
    root = tk.Tk()
    app = UARTGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()

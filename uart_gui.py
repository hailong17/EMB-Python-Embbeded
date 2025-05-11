import tkinter as tk
from tkinter import ttk
from uart_handler import UARTHandler
from utils import auto_detect_port

class UARTGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("UART Console Tool")
        self.master.geometry("400x300")

        # Thêm nút tự động phát hiện cổng UART
        self.auto_detect_button = tk.Button(self.master, text="Auto Detect Port", command=self.auto_detect_uart)
        self.auto_detect_button.pack(pady=10)

        # Các phần còn lại của giao diện
        self.port_var = tk.StringVar()
        self.uart = None

        self.create_widgets()

    def create_widgets(self):
        # Label và ComboBox để chọn cổng
        self.port_label = tk.Label(self.master, text="Select Port:")
        self.port_label.pack(pady=10)

        self.port_combobox = ttk.Combobox(self.master, textvariable=self.port_var, values=["COM3", "COM4", "COM5"])
        self.port_combobox.pack()

        # Nút mở kết nối UART
        self.connect_button = tk.Button(self.master, text="Open UART", command=self.open_uart)
        self.connect_button.pack(pady=10)

        # Nút gửi lệnh
        self.command_entry = tk.Entry(self.master)
        self.command_entry.pack(pady=5)

        self.send_button = tk.Button(self.master, text="Send Command", command=self.send_command)
        self.send_button.pack(pady=10)

        # Kết quả gửi/nhận
        self.result_label = tk.Label(self.master, text="Results will be shown here.")
        self.result_label.pack(pady=10)

        # Nút đóng kết nối UART
        self.close_button = tk.Button(self.master, text="Close UART", command=self.close_uart)
        self.close_button.pack(pady=10)

    def auto_detect_uart(self):
        try:
            # Sử dụng hàm auto_detect_port từ utils.py để tự động phát hiện cổng
            detected_port = auto_detect_port()
            self.port_var.set(detected_port)
            print(f"✔️ Automatically detected UART on {detected_port}")
            self.open_uart()
        except Exception as e:
            print(str(e))
            self.result_label.config(text="❌ Error auto-detecting port!")

    def open_uart(self):
        port = self.port_var.get()
        self.uart = UARTHandler(port=port)
        self.uart.open()
        self.result_label.config(text=f"✔️ Opened UART on {port}")

    def send_command(self):
        command = self.command_entry.get()
        if command and self.uart and self.uart.is_open():
            self.uart.send(command)
        else:
            self.result_label.config(text="❌ Please open the UART first!")

    def close_uart(self):
        if self.uart:
            self.uart.close()
            self.result_label.config(text="❎ Closed UART.")
        else:
            self.result_label.config(text="❌ No UART connection to close.")

def main():
    root = tk.Tk()
    app = UARTGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()

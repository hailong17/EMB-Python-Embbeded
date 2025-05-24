import tkinter as tk
from tkinter import ttk
from uart_handler import UARTHandler
from utils import SerialPortManager
import serial


class UARTGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("UART Console Tool")
        self.master.geometry("500x600")

        # Biến lưu UART handler
        self.uart = UARTHandler()

        self.port_var = tk.StringVar()
        self.baud_var = tk.StringVar(value="115200")

        self.data_bits_var = tk.StringVar(value="8")
        self.stop_bits_var = tk.StringVar(value="1")
        self.parity_var = tk.StringVar(value="None")
        self.flow_control_var = tk.StringVar(value="None")


        self.create_widgets()

    def create_widgets(self):
        tk.Button(self.master, text="Auto Detect Port", command=self.auto_detect_uart).pack(pady=10)

        tk.Label(self.master, text="Select Port:").pack()
        self.port_combobox = ttk.Combobox(self.master, textvariable=self.port_var)
        self.port_combobox.pack()

        tk.Label(self.master, text="Select Baudrate:").pack()
        baudrates = ["9600", "19200", "38400", "57600", "115200", "230400", "460800", "921600"]
        self.baud_combobox = ttk.Combobox(self.master, textvariable=self.baud_var, values=baudrates)
        self.baud_combobox.pack(pady=5)

        # Data Bits
        tk.Label(self.master, text="Data Bits:").pack()
        data_bits_options = ["5", "6", "7", "8"]
        ttk.Combobox(self.master, textvariable=self.data_bits_var, values=data_bits_options).pack()

        # Stop Bits
        tk.Label(self.master, text="Stop Bits:").pack()
        stop_bits_options = ["1", "1.5", "2"]
        ttk.Combobox(self.master, textvariable=self.stop_bits_var, values=stop_bits_options).pack()

        # Parity
        tk.Label(self.master, text="Parity:").pack()
        parity_options = ["None", "Even", "Odd", "Mark", "Space"]
        ttk.Combobox(self.master, textvariable=self.parity_var, values=parity_options).pack()

        # Flow Control
        tk.Label(self.master, text="Flow Control:").pack()
        flow_control_options = ["None", "RTS/CTS", "XON/XOFF"]
        ttk.Combobox(self.master, textvariable=self.flow_control_var, values=flow_control_options).pack()
        
        tk.Button(self.master, text="Open UART", command=self.open_uart).pack(pady=10)

        self.command_entry = tk.Entry(self.master)
        self.command_entry.pack(pady=5)

        tk.Button(self.master, text="Send Command", command=self.send_command).pack(pady=10)

        self.result_label = tk.Label(self.master, text="Results will be shown here.")
        self.result_label.pack(pady=10)

        tk.Button(self.master, text="Close UART", command=self.close_uart).pack(pady=10)

    def auto_detect_uart(self):
        try:
            manager = SerialPortManager()
            detected_port = manager.auto_detect_port()
            self.port_var.set(detected_port)
            print(f"✔️ Automatically detected UART on {detected_port}")
            self.open_uart()
        except Exception as e:
            print(str(e))
            self.result_label.config(text="❌ Error auto-detecting port!")

    def open_uart(self):
        port = self.port_var.get()
        baud = int(self.baud_var.get())

        # Lấy cấu hình nâng cao
        data_bits = int(self.data_bits_var.get())
        stop_bits = float(self.stop_bits_var.get())
        parity = self.parity_var.get()
        flow = self.flow_control_var.get()

        # Mapping parity
        parity_map = {
        "None": serial.PARITY_NONE,
        "Even": serial.PARITY_EVEN,
        "Odd": serial.PARITY_ODD,
        "Mark": serial.PARITY_MARK,
        "Space": serial.PARITY_SPACE
        }

        # Mapping stop bits
        stop_bits_map = {
        1: serial.STOPBITS_ONE,
        1.5: serial.STOPBITS_ONE_POINT_FIVE,
        2: serial.STOPBITS_TWO
        }

        # Mapping flow control
        rtscts = flow == "RTS/CTS"
        xonxoff = flow == "XON/XOFF"

        self.uart.select_baud(baud)
        self.uart.open(
        port,
        bytesize=data_bits,
        stopbits=stop_bits_map[stop_bits],
        parity=parity_map[parity],
        rtscts=rtscts,
        xonxoff=xonxoff
    )

        if self.uart.is_open():
            self.result_label.config(text=f"✔️ UART opened on {port} @ {baud}bps")
        else:
            self.result_label.config(text="❌ Failed to open UART.")


    def send_command(self):
        cmd = self.command_entry.get()
        if cmd and self.uart and self.uart.is_open():
            self.uart.write(cmd + "\r\n")
            resp = self.uart.read()
            if resp:
                self.result_label.config(text=f"← {resp.strip().decode(errors='ignore')}")
            else:
                self.result_label.config(text="❌ No response received.")
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

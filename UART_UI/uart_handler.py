import serial
import time

class UARTHandler:
    def __init__(self, baudrate=115200, timeout=1, **kwargs):
        self.port = None
        self.baudrate = baudrate
        self.timeout = timeout
        self.ser = None
        self.kwargs = kwargs

    def select_baud(self, baudrate_from_gui):
        self.baudrate = baudrate_from_gui
        print(f"✔️ Selected baudrate: {self.baudrate}")

    def open(self, port, **kwargs):
        self.port = port
        try:
            self.ser = serial.Serial(
            port=self.port,
            baudrate=self.baudrate,
            timeout=self.timeout,
            **kwargs
            )
            print(f"✔️ Opened UART on {self.port} @ {self.baudrate}bps")
        except serial.SerialException as e:
            print(f"❌ Error opening port {self.port}: {e}")
            self.ser = None


    def close(self):
        if self.ser and self.ser.is_open:
            self.ser.close()
            print(f"❎ Closed UART on {self.port}")
        else:
            print("❎ UART is not open.")

    def write(self, data):
        if self.ser and self.ser.is_open:
            if isinstance(data, str):
                data = data.encode('utf-8')
            self.ser.write(data)
            print(f"→ Sent: {data}")
        else:
            print("❌ UART is not open. Please open the port first.")

    def read(self):
        if self.ser and self.ser.is_open:
            try:
                resp = self.ser.readline()
                print(f"← Received: {resp}")
                return resp
            except Exception as e:
                print(f"❌ Error reading from UART: {e}")
                return None
        else:
            print("❌ UART is not open. Please open the port first.")
            return None

    def is_open(self):
        return self.ser and self.ser.is_open

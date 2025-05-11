import serial
import time

class UARTHandler:
    def __init__(self, port, baudrate=115200, timeout=1, **kwargs):
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.ser = None
        self.kwargs = kwargs

    def open(self):
        try:
            # Mở cổng UART với các tham số cấu hình
            self.ser = serial.Serial(port=self.port,
                                     baudrate=self.baudrate,
                                     timeout=self.timeout,
                                     **self.kwargs)
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

    def send(self, data):
        if self.ser and self.ser.is_open:
            if isinstance(data, str):
                data = data.encode('utf-8')
            self.ser.write(data)
            print(f"→ Sent: {data}")
            # Chờ phản hồi
            time.sleep(0.1)
            resp = self.ser.readline()
            print(f"← Received: {resp}")
        else:
            print("❌ UART is not open. Please open the port first.")

    def is_open(self):
        return self.ser and self.ser.is_open

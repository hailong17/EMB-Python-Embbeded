import serial
import serial.tools.list_ports
import time

class SerialPortManager:
    PREFERRED_VID_PID = [
        ("1A86", "7523"),  # CH340
        ("10C4", "EA60"),  # CP210x
        ("0483", "5740"),  # ST-Link VCP
    ]

    def __init__(self, test_cmd="ping", baudrate=115200, timeout=1):
        self.test_cmd = test_cmd
        self.baudrate = baudrate
        self.timeout = timeout

    def list_ports(self):
        return list(serial.tools.list_ports.comports())

    def test_command(self, port):
        print(f"🔍 Testing port {port} with command '{self.test_cmd}' @ {self.baudrate}bps...")
        try:
            with serial.Serial(port=port, baudrate=self.baudrate, timeout=self.timeout) as ser:
                ser.reset_input_buffer()
                ser.write((self.test_cmd + "\r\n").encode())
                time.sleep(0.2)
                resp = ser.readline()
                if resp:
                    decoded = resp.strip().decode(errors='ignore')
                    print(f"✔️ Response from {port}: {decoded}")
                    return True
                else:
                    print(f"⚠️ No response from {port}")
        except serial.SerialException as e:
            print(f"❌ Serial error on {port}: {e}")
        except Exception as e:
            print(f"❌ Unexpected error on {port}: {e}")
        return False

    def auto_detect_port(self):
        try:
            ports = self.list_ports()
        except Exception:
            raise Exception("⚠️ No serial ports found!")

        # Ưu tiên theo VID:PID
        for p in ports:
            if p.vid is not None and p.pid is not None:
                vid_pid = (f"{p.vid:04X}", f"{p.pid:04X}")
                if vid_pid in self.PREFERRED_VID_PID:
                    print(f"📌 Preferred device found: {p.device} ({vid_pid[0]}:{vid_pid[1]})")
                    return p.device

        # Ưu tiên thiết bị có "USB" hoặc "UART" trong mô tả
        for p in ports:
            if "USB" in p.description or "UART" in p.description:
                print(f"📌 USB/UART device found: {p.device} ({p.description})")
                return p.device

        # Không có gì đặc biệt, chọn thiết bị đầu tiên
        if ports:
            print(f"📌 Fallback to first available port: {ports[0].device}")
            return ports[0].device
        else:
            raise Exception("❌ No available serial ports.")


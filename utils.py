import serial.tools.list_ports

def list_ports():
    return list(serial.tools.list_ports.comports())

def auto_detect_port():
    ports = list_ports()
    if not ports:
        raise Exception("⚠️ No serial ports found!")

    for p in ports:
        if "USB" in p.description or "UART" in p.description:
            return p.device
    return ports[0].device

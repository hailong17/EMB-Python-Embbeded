import tkinter as tk
from tkinter import messagebox
import threading
import time
import psutil
import pygetwindow as gw
import pyautogui


class TeamsCameraAutoToggleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Auto Camera Off for Teams")
        self.root.geometry("300x250")
        self.running = False

        self.label = tk.Label(root, text="Auto Camera Control", font=("Arial", 14))
        self.label.pack(pady=10)

        self.status_label = tk.Label(root, text="Status: Stopped", fg="red")
        self.status_label.pack(pady=5)

        self.toggle_button = tk.Button(root, text="Start Monitoring", width=20, command=self.toggle_monitoring)
        self.toggle_button.pack(pady=10)

        self.manual_off_button = tk.Button(root, text="Tắt Camera Ngay", width=20, command=self.toggle_camera_manually)
        self.manual_off_button.pack(pady=10)

        self.quit_button = tk.Button(root, text="Quit", width=20, command=self.root.quit)
        self.quit_button.pack(pady=10)

    def toggle_monitoring(self):
        if not self.running:
            self.running = True
            self.status_label.config(text="Status: Running", fg="green")
            self.toggle_button.config(text="Stop Monitoring")
            threading.Thread(target=self.monitor_loop, daemon=True).start()
        else:
            self.running = False
            self.status_label.config(text="Status: Stopped", fg="red")
            self.toggle_button.config(text="Start Monitoring")

    def toggle_camera_manually(self):
        try:
            pyautogui.hotkey('ctrl', 'shift', 'o')
            messagebox.showinfo("Camera Toggled", "Đã gửi Ctrl + Shift + O để tắt/mở camera.")
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể gửi phím tắt: {e}")

    def monitor_loop(self):
        already_toggled = False
        while self.running:
            if self.is_teams_running():
                win = self.find_meeting_window()
                if win and not already_toggled:
                    win.activate()
                    time.sleep(1)
                    pyautogui.hotkey('ctrl', 'shift', 'o')
                    print("[INFO] Đã gửi Ctrl + Shift + O")
                    already_toggled = True
            else:
                already_toggled = False
            time.sleep(5)

    def is_teams_running(self):
        for proc in psutil.process_iter(['name']):
            try:
                if proc.info['name'] and 'Teams' in proc.info['name']:
                    return True
            except:
                continue
        return False

    def find_meeting_window(self):
        for w in gw.getWindowsWithTitle("Microsoft Teams"):
            if "Meeting" in w.title or "Microsoft Teams" in w.title:
                return w
        return None


if __name__ == "__main__":
    root = tk.Tk()
    app = TeamsCameraAutoToggleApp(root)
    root.mainloop()

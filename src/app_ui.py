import tkinter as tk
import threading
from main import run_assistant

running = False

def start():
    global running
    if not running:
        running = True
        threading.Thread(target=run_assistant).start()

def stop():
    global running
    running = False

def create_ui():
    root = tk.Tk()
    root.title("AI Blind Assistant")
    root.geometry("300x200")

    start_btn = tk.Button(root, text="Start", command=start, bg="green", fg="white", height=2)
    start_btn.pack(pady=20)

    stop_btn = tk.Button(root, text="Stop", command=stop, bg="red", fg="white", height=2)
    stop_btn.pack(pady=20)

    root.mainloop()
import cv2
import threading
from camera import start_camera
from detector import detect_objects
from voice_engine import speak, alert
from navigation import navigate
from voice_commands import listen
from ocr_reader import read_text
from ai_description import describe

cap = start_camera()
if cap is None:
    exit()

speak("System started")

# ✅ Voice command runs in background — doesn't block camera
current_command = [None]  # list so we can modify inside thread

def voice_listener():
    while True:
        command = listen()
        if command:
            current_command[0] = command

threading.Thread(target=voice_listener, daemon=True).start()

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ Frame error")
        break

    # 🎯 Object Detection
    objects, frame = detect_objects(frame)

    for name, area, x1, x2 in objects:
        alert(name)

    # 🧭 Navigation
    frame_width = frame.shape[1]
    direction = navigate(objects, frame_width)
    if direction:
        speak(direction)

    # 🎤 Voice Commands (non-blocking)
    command = current_command[0]
    if command:
        current_command[0] = None  # reset after reading

        if "read" in command:
            text = read_text(frame)
            if text:
                speak(text)

        elif "describe" in command:
            caption = describe(frame)
            speak(caption)

        elif "stop" in command:
            speak("Stopping program")
            break

    # 🎨 UI
    cv2.putText(frame, "AI Blind Assistant", (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Camera", frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
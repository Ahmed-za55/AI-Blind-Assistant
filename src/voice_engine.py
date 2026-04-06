import pyttsx3
import threading
import time

engine = pyttsx3.init()
engine.setProperty('rate', 150)
lock = threading.Lock()

_last_spoken = {}
COOLDOWN_SECONDS = 3

def speak(text):
    def run():
        with lock:
            print("Assistant:", text)
            engine.say(text)
            engine.runAndWait()
    threading.Thread(target=run, daemon=True).start()


def alert(object_name):
    now = time.time()
    last = _last_spoken.get(object_name, 0)

    if now - last < COOLDOWN_SECONDS:
        return

    _last_spoken[object_name] = now

    if object_name == "person":
        speak("Person detected")
    elif object_name == "cell phone":
        speak("Phone detected")
    else:
        speak(f"{object_name} detected")
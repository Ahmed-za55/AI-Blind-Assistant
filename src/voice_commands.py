import speech_recognition as sr

recognizer = sr.Recognizer()

def listen():
    """
    Listens to microphone and returns recognized command as lowercase string.
    Returns None if nothing is heard or recognition fails.
    """
    with sr.Microphone() as source:
        try:
            # Adjust for background noise quickly
            recognizer.adjust_for_ambient_noise(source, duration=0.5)

            print("🎤 Listening...")
            # timeout=2  → stop waiting after 2 seconds of silence
            # phrase_time_limit=4 → max 4 seconds per command
            audio = recognizer.listen(source, timeout=2, phrase_time_limit=4)

            command = recognizer.recognize_google(audio).lower()
            print(f"✅ Command heard: {command}")
            return command

        except sr.WaitTimeoutError:
            # No speech detected — normal, just return None
            return None
        except sr.UnknownValueError:
            # Speech detected but couldn't understand
            return None
        except sr.RequestError as e:
            print(f"❌ Google Speech API error: {e}")
            return None
        except Exception as e:
            print(f"❌ Microphone error: {e}")
            return None
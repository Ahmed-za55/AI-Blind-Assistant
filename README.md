# 🦯 AI Blind Assistant

> An intelligent real-time assistant that helps visually impaired people navigate their surroundings using Computer Vision, AI, and Voice Feedback.

![Python](https://img.shields.io/badge/Python-3.11-blue?style=flat-square&logo=python)
![YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-purple?style=flat-square)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green?style=flat-square&logo=opencv)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)

---

## 📖 Overview

**AI Blind Assistant** is a Python-based real-time assistive system designed for visually impaired individuals. It uses a camera to continuously analyze the environment and provides spoken feedback about detected objects, their positions, and potential dangers — all hands-free through voice commands.

---

## ✨ Features

| Feature | Description |
|---|---|
| 👁️ **Object Detection** | Detects 80+ object types in real-time using YOLOv8 |
| 🔊 **Voice Alerts** | Speaks detected objects and navigation directions instantly |
| 🧭 **Navigation System** | Warns about nearby obstacles (left / right / ahead / too close) |
| 📖 **OCR Text Reading** | Reads text from signs, books, or screens using Tesseract |
| 🧠 **Scene Description** | Describes the full scene using BLIP AI model |
| 🎤 **Voice Commands** | Control the assistant hands-free ("read", "describe", "stop") |
| ⏱️ **Smart Cooldown** | Prevents repetitive alerts — speaks each object every 3 seconds max |

---

## 🗂️ Project Structure

```
AI-Blind-Assistant/
│
├── src/
│   ├── main.py              # Entry point — main loop
│   ├── camera.py            # Camera initialization
│   ├── detector.py          # YOLOv8 object detection
│   ├── navigation.py        # Direction & proximity logic
│   ├── voice_engine.py      # Text-to-speech + smart alerts
│   ├── voice_commands.py    # Speech recognition (microphone input)
│   ├── ocr_reader.py        # Tesseract OCR text extraction
│   ├── ai_description.py    # BLIP scene captioning
│   ├── app_ui.py            # Tkinter UI (Start / Stop buttons)
│   └── utils.py             # Frame saving utility
│
├── models/
│   └── yolov8n.pt           # YOLOv8 nano model (auto-downloaded)
│
├── requirements.txt
└── README.md
```

---

## 🧠 Tech Stack

- **[Python 3.11](https://www.python.org/)** — Core language
- **[YOLOv8](https://github.com/ultralytics/ultralytics)** — Real-time object detection
- **[OpenCV](https://opencv.org/)** — Camera feed & image processing
- **[BLIP](https://huggingface.co/Salesforce/blip-image-captioning-base)** — AI scene description (Hugging Face Transformers)
- **[Tesseract OCR](https://github.com/tesseract-ocr/tesseract)** — Text extraction from images
- **[pyttsx3](https://pypi.org/project/pyttsx3/)** — Offline text-to-speech
- **[SpeechRecognition](https://pypi.org/project/SpeechRecognition/)** — Voice command input
- **[PyAudio](https://pypi.org/project/PyAudio/)** — Microphone access

---

## ⚙️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/Ahmed-za55/AI-Blind-Assistant.git
cd AI-Blind-Assistant
```

### 2. Create a virtual environment
```bash
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Linux / macOS
```

### 3. Install Python dependencies
```bash
pip install -r requirements.txt
```

### 4. Install Tesseract OCR
Download and install from: https://github.com/tesseract-ocr/tesseract

Then update the path in `src/ocr_reader.py`:
```python
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```

### 5. Run the assistant
```bash
cd src
python main.py
```

---

## 🎤 Voice Commands

Once running, you can speak these commands:

| Command | Action |
|---|---|
| `"read"` | Reads any visible text using OCR |
| `"describe"` | Describes the full scene using AI |
| `"stop"` | Stops the program |

---

## 🧭 How Navigation Works

The frame is divided into 3 zones:

```
|   LEFT   |   CENTER   |   RIGHT   |
|  < 1/3   |    mid     |  > 2/3    |
```

- Object area > 60,000 px → **"Stop! [object] very close"**
- Object in left zone → **"[object] on your left"**
- Object in right zone → **"[object] on your right"**
- Object in center → **"[object] ahead"**

---

## 📸 Demo

> Camera detects objects → Voice speaks directions → User navigates safely

```
✅ Camera connected
Assistant: System started
Assistant: Person detected
Assistant: Stop! person very close
Assistant: laptop on your right
🎤 Listening...
✅ Command heard: describe
Assistant: a person sitting at a desk with a laptop
```

---

## 🚧 Known Limitations

- Scene description (BLIP) requires internet for first-time model download (~1GB)
- OCR works best with clear, printed English text
- Voice commands require an active internet connection (Google Speech API)
- Performance depends on CPU speed — GPU recommended for faster detection

---

## 🔮 Future Improvements

- [ ] Add Arabic language support for OCR and voice
- [ ] Offline voice commands using VOSK
- [ ] GPS + map integration for outdoor navigation
- [ ] Mobile app version (Android)
- [ ] Depth estimation for better distance detection

---

## 👨‍💻 Author

**Ahmed Sameh Sharaf**  
Faculty of Artificial Intelligence — Kafrelsheikh University  
📧 Connect on [LinkedIn](https://) | [GitHub](https://github.com/Ahmed-za55/Ahmed-za55)

---

## 📄 License

This project is licensed under the MIT License — feel free to use and build upon it.

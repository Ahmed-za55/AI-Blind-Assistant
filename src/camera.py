import cv2

def start_camera():
    cap = cv2.VideoCapture(0)  # 👈 مهم

    if not cap.isOpened():
        print("❌ Camera not working")
        return None

    print("✅ Camera connected")

    return cap
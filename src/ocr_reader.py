import pytesseract
import cv2

# السطر ده هو "الجسر" بين بايثون والبرنامج اللي سطبته
# r قبل علامة التنصيص مهمة جداً عشان الويندوز يفهم المسار صح
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def read_text(frame):
    try:
        # 1. تحويل الصورة للأبيض والأسود (رمادي) عشان الحروف تبان
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # 2. تنقية الصورة من الشوشرة (Thresholding)
        gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
        
        # 3. استخراج النص
        text = pytesseract.image_to_string(gray, lang='eng') # حالياً بيقرأ إنجليزي
        return text.strip()
    except Exception as e:
        print(f"OCR Error: {e}")
        return ""
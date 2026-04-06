from PIL import Image
import torch

# ✅ FIX: Lazy loading — model loads only when describe() is called for the first time
# This prevents slow startup when the feature isn't needed
_processor = None
_model = None

def _load_model():
    global _processor, _model
    if _processor is None:
        print("⏳ Loading BLIP model (first time only)...")
        from transformers import BlipProcessor, BlipForConditionalGeneration
        _processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
        _model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
        print("✅ BLIP model loaded")


def describe(frame):
    _load_model()

    image = Image.fromarray(frame)
    inputs = _processor(image, return_tensors="pt")

    with torch.no_grad():
        out = _model.generate(**inputs)

    caption = _processor.decode(out[0], skip_special_tokens=True)
    return caption




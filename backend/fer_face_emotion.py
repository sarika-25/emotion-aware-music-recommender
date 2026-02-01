from PIL import Image
import io

def detect_face_emotion(image_bytes):
    try:
        image = Image.open(io.BytesIO(image_bytes)).convert("L")
        pixels = list(image.getdata())
        avg_brightness = sum(pixels) / len(pixels)

        # Extended heuristic mapping (still simple & stable)
        if avg_brightness >= 180:
            return "surprised"
        elif 150 <= avg_brightness < 180:
            return "happy"
        elif 125 <= avg_brightness < 150:
            return "calm"
        elif 100 <= avg_brightness < 125:
            return "neutral"
        elif 80 <= avg_brightness < 100:
            return "angry"
        elif 60 <= avg_brightness < 80:
            return "sad"
        else:
            return "depressed"

    except Exception:
        return "neutral"

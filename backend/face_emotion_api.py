import requests

# 🔴 PUT YOUR RAPIDAPI KEY HERE
RAPIDAPI_KEY = "3f2cd9808msh01ddcc1284510bcp154c77jsna0969b9e23a61"
RAPIDAPI_HOST = "faceanalyzer-ai.p.rapidapi.com"


def detect_face_emotion(image_bytes):
    url = "https://faceanalyzer-ai.p.rapidapi.com/faceanalysis"

    headers = {
        "X-RapidAPI-Key": RAPIDAPI_KEY,
        "X-RapidAPI-Host": RAPIDAPI_HOST
    }

    files = {
        "image": ("image.jpg", image_bytes, "image/jpeg")
    }

    response = requests.post(url, headers=headers, files=files)
    data = response.json()

    try:
        emotion = data["body"]["faces"][0]["facialFeatures"]["Emotions"][0]
        return emotion.lower()
    except Exception:
        return "neutral"
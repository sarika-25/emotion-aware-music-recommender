from transformers import pipeline
import streamlit as st

# ---------------- EMOTION MAPPING ----------------
EMOTION_MAPPING = {
    'joy': 'happy',
    'love': 'happy',
    'excitement': 'happy',
    'amusement': 'happy',

    'interest': 'neutral',
    'satisfaction': 'neutral',
    'calmness': 'neutral',

    'sadness': 'sad',

    'anger': 'angry',
    'disgust': 'angry',

    'fear': 'fear',
    'surprise': 'surprise'
}

# ---------------- LOAD MODEL (CACHED) ----------------
@st.cache_resource
def load_text_model():
    return pipeline(
        "text-classification",
        model="ayoubkirouane/BERT-Emotions-Classifier",
        device=-1  # CPU safe
    )

TEXT_CLASSIFIER = load_text_model()

# ---------------- MAIN FUNCTION ----------------
def detect_text_emotion(text: str) -> str:
    if not text.strip():
        return "neutral"

    output = TEXT_CLASSIFIER(text, top_k=1)[0]

    # Confidence threshold
    if output["score"] < 0.55:
        return "neutral"

    raw_emotion = output["label"].lower()
    return EMOTION_MAPPING.get(raw_emotion, "neutral")

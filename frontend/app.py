import sys
import os
import streamlit as st
from collections import deque, Counter

# ---------------- PATH FIX ----------------
sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)

from backend.text_models import detect_text_emotion
from backend.fer_face_emotion import detect_face_emotion
from backend.music_recommender import recommend_songs_by_emotion

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Emotion → Music Recommender",
    layout="wide"
)

# ---------------- EMOTION SMOOTHING ----------------
emotion_buffer = deque(maxlen=5)

def smooth_emotion(new_emotion):
    emotion_buffer.append(new_emotion)
    return Counter(emotion_buffer).most_common(1)[0][0]

# ---------------- UI STYLES ----------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(
        135deg,
        #0f2027,
        #203a43,
        #2c5364,
        #6a11cb,
        #2575fc
    );
    background-size: 400% 400%;
    animation: gradientBG 15s ease infinite;
}
@keyframes gradientBG {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}
.card {
    background: rgba(0,0,0,0.45);
    padding: 30px;
    border-radius: 22px;
    margin-bottom: 22px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.title("🎧 Emotion → Music Recommender")
st.write("Detect emotion from **text or image** and get music instantly.")
st.markdown("</div>", unsafe_allow_html=True)

uplift = st.checkbox("⭐ Cheer me up!")

tab1, tab2 = st.tabs(["📝 Text Input", "📷 Image Upload"])
detected_emotion = None

# ---------------- TEXT TAB ----------------
with tab1:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    text = st.text_area("Type how you feel")

    if st.button("Analyze Text"):
        raw = detect_text_emotion(text)
        detected_emotion = smooth_emotion(raw)
        st.success(f"Detected Emotion: {detected_emotion}")

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- IMAGE TAB ----------------
with tab2:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    image = st.file_uploader("Upload face image", ["jpg", "jpeg", "png"])

    if image and st.button("Analyze Image"):
        raw = detect_face_emotion(image.read())
        detected_emotion = smooth_emotion(raw)
        st.success(f"Detected Emotion: {detected_emotion}")
        st.image(image, width=260)

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- SONGS ----------------
if detected_emotion:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("🎵 Recommended Songs")

    st.info("⚠️ Emotion is inferred from observable cues and may not reflect true emotional state.")

    songs = recommend_songs_by_emotion(detected_emotion, uplift=uplift)

    for song in songs:
        st.markdown(f"**{song['name']}** — {song['artist']}")
        embed = f"""
        <iframe src="https://open.spotify.com/embed/track/{song['spotify_id']}"
                width="100%" height="80" frameborder="0"
                allow="autoplay; encrypted-media"></iframe>
        """
        st.components.v1.html(embed, height=90)

    st.markdown("</div>", unsafe_allow_html=True)

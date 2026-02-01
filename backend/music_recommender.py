import pandas as pd
import os

BASE_DIR = os.path.dirname(__file__)
CSV_PATH = os.path.join(BASE_DIR, "data", "Music_Info.csv")

music_df = pd.read_csv(CSV_PATH)

def recommend_songs_by_emotion(emotion, uplift=False, n=5):
    emotion = emotion.lower()

    # Uplift logic (context-aware)
    if uplift and emotion in ["sad", "angry", "depressed"]:
        emotion = "happy"

    if emotion in music_df.columns:
        filtered = music_df[music_df[emotion] == 1]
    else:
        filtered = music_df

    if filtered.empty:
        filtered = music_df

    songs = filtered.sample(min(n, len(filtered)))

    return [
        {
            "name": row["name"],
            "artist": row["artist"],
            "spotify_id": row["spotify_id"]
        }
        for _, row in songs.iterrows()
    ]

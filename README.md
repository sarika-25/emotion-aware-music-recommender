# 🎧 Emotion-Aware Music Recommendation System

##
A real-time applied AI system that detects user emotions from **text or facial images** and recommends music accordingly.  
The system treats emotion as a **contextual and noisy signal**, focusing on stability and responsible recommendations rather than perfect emotion prediction.

## Features
- Emotion detection from text using transformer-based NLP models  
- Facial emotion analysis using image-based affect cues with fallback mechanisms  
- Context-aware music recommendation with optional uplift mode  
- Emotion smoothing and confidence thresholds for stable predictions  
- Interactive Streamlit web interface with Spotify music embeds  

## Tech Stack
Python, Transformers (BERT), Streamlit, Pandas, Spotify Embed

## How to Run
```bash
pip install -r requirements.txt
streamlit run frontend/app.py

import streamlit as st
import random
from textblob import TextBlob
import requests
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

API_BASE_URL = "http://localhost:5000/api"
import streamlit as st

def load_css():
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()
# Initialize sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# Sample Recommendations
recommendations = {
    "happy": {
        "books": ["The Alchemist", "The Happiness Project"],
        "songs": ["Happy - Pharrell Williams", "Can't Stop the Feeling"],
        "movies": ["Inside Out", "Forrest Gump"]
    },
    "sad": {
        "books": ["Reasons to Stay Alive", "The Fault in Our Stars"],
        "songs": ["Someone Like You - Adele", "Fix You - Coldplay"],
        "movies": ["The Pursuit of Happyness", "A Beautiful Mind"]
    },
    "neutral": {
        "books": ["Atomic Habits", "Deep Work"],
        "songs": ["Blinding Lights - The Weeknd", "Shape of You - Ed Sheeran"],
        "movies": ["Inception", "Interstellar"]
    }
}

# Streamlit UI
st.title("BinaryHug")
st.write("Describe how you're feeling today, and I'll recommend books, songs, and movies!")


user_input = st.text_area("Enter your feelings:")

if st.button("Get Recommendations"):
    if user_input:
        
        sentiment_score = analyzer.polarity_scores(user_input)['compound']

       
        if sentiment_score >= 0.2:
            mood = "happy"
        elif sentiment_score <= -0.2:
            mood = "sad"
        else:
            mood = "neutral"


       

        book_response=requests.get(f"{API_BASE_URL}/{mood}/books")
        movie_response=requests.get(f"{API_BASE_URL}/{mood}/movies")
        song_response=requests.get(f"{API_BASE_URL}/{mood}/songs")


        book_data=book_response.json()
        movie_data=movie_response.json()
        song_data=song_response.json()

        
        st.subheader(f"Detected Mood: **{mood.capitalize()}**")

        
        recs = recommendations[mood]

        st.subheader("📚 Try Reading:")
        st.write(book_data["recommendation"])

        st.subheader("🎵 Listen to:")
        st.write(song_data["recommendation"])

        st.subheader("🎬 Watch:")
        st.write(movie_data["recommendation"])

    else:
        st.warning("Please enter some text to analyze your mood.")

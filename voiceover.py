import streamlit as st
from gtts import gTTS
import os

# Function to convert text to speech using gTTS
def text_to_speech(text, lang):
    tts = gTTS(text=text, lang=lang, slow=False)
    output_file = "output.mp3"
    tts.save(output_file)
    return output_file

# Streamlit user interface
st.title("Text to Speech Converter")

text = st.text_area("Enter text here:", "Type the text you want to convert to speech here...")
lang = st.selectbox("Select language:", ["en", "ar", "fr", "es", "de"])

if st.button("Convert Text to Speech"):
    if text.strip() == "":
        st.error("Please enter some text.")
    else:
        output_file = text_to_speech(text, lang)
        st.audio(output_file, format="audio/mp3")
    
    # Optional: Delete the audio file after use
    if os.path.exists(output_file):
        os.remove(output_file)

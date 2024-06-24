import streamlit as st
from gtts import gTTS
import os
from pydub import AudioSegment
from pydub.utils import which

# Ensure ffmpeg is available
ffmpeg_path = which("ffmpeg")
if ffmpeg_path is None:
    st.error("Please Try Again Later")
else:
    AudioSegment.converter = ffmpeg_path

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
        try:
            audio = AudioSegment.from_mp3(output_file)
            st.audio(output_file, format="audio/mp3")
        except Exception as e:
            st.error(f"Error loading audio file: {e}")
    
    # Optional: Delete the audio file after use
    if os.path.exists("output.mp3"):
        os.remove("output.mp3")
# CSS مخصص لإخفاء الروابط عند تمرير الفأرة
hide_links_style = """
    <style>
    a {
        text-decoration: none;
        color: inherit;
        pointer-events: none;
    }
    a:hover {
        text-decoration: none;
        color: inherit;
        cursor: default;
    }
    </style>
    """
st.markdown(hide_links_style, unsafe_allow_html=True)
from gtts import gTTS
import streamlit as st
import io

text = "hello"

speech = gTTS(text, lang='en', slow=False)

audio_buffer = io.BytesIO()
speech.write_to_fp(audio_buffer)

st.audio(audio_buffer)








# import streamlit as st
# from api_calling import text_to_speech


# st.title("Audio Test")

# text = st.text_area("Enter text to convert into audio")

# if st.button("Generate Audio"):
#     if text:
#         audio = text_to_speech(text)
#         st.audio(audio, format="audio/mp3")
#     else:
#         st.error("Please enter some text.")
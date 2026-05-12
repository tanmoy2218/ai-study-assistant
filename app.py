import streamlit as st
from PIL import Image, UnidentifiedImageError

from api_calling import generate_notes, audio_transcription, generate_quiz


st.set_page_config(
    page_title="AI Study Assistant",
    page_icon="🧠",
    layout="wide"
)

st.markdown("""
<style>
.main-title {
    font-size: 42px;
    font-weight: 800;
    text-align: center;
}
.subtitle {
    font-size: 18px;
    text-align: center;
    color: gray;
}
.card {
    padding: 20px;
    border-radius: 15px;
    background-color: #f8f9fa;
}
</style>
""", unsafe_allow_html=True)


st.markdown('<div class="main-title">📚 AI Study Assistant</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">🧠 Your smart learning companion</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Upload note images, generate summaries, listen as audio, and create quizzes.</div>',
    unsafe_allow_html=True
)

st.divider()


with st.sidebar:
    st.header("⚙️ Controls")

    uploaded_images = st.file_uploader(
        "Upload note images(Max 3)",
        type=["jpg", "jpeg", "png"],
        accept_multiple_files=True
    )

    difficulty = st.selectbox(
        "Select quiz difficulty",
        ["Easy", "Medium", "Hard"],
        index=None
    )

    generate_button = st.button("🚀 Generate Study Materials", type="primary")


pil_images = []

if uploaded_images:
    if len(uploaded_images) > 3:
        st.error("You can upload maximum 3 images only.")
        st.stop()

    st.subheader("📷 Uploaded Images")

    columns = st.columns(len(uploaded_images))

    for index, uploaded_file in enumerate(uploaded_images):
        try:
            image = Image.open(uploaded_file).convert("RGB")
            pil_images.append(image)

            with columns[index]:
                st.image(image, caption=f"Image {index + 1}", use_container_width=True)

        except UnidentifiedImageError:
            st.error(f"{uploaded_file.name} is not a valid image file.")
            st.stop()


if generate_button:
    if not uploaded_images:
        st.error("Please upload at least 1 image.")
        st.stop()

    if not difficulty:
        st.error("Please select quiz difficulty.")
        st.stop()

    try:
        with st.spinner("AI is generating your notes..."):
            notes = generate_notes(pil_images)

        st.success("Notes generated successfully!")

        with st.container(border=True):
            st.subheader("📝 Generated Notes")
            st.markdown(notes)

            st.download_button(
                label="⬇️ Download Notes",
                data=notes,
                file_name="generated_notes.txt",
                mime="text/plain"
            )


        with st.container(border=True):
            st.subheader("Audio Transcription")

            #the portion below will be replaced by API Call
            with st.spinner("AI is generating audio of this note"):

                #clearing the markdown

                notes = notes.replace("#","")
                notes = notes.replace("*","")
                notes = notes.replace("-","")
                notes = notes.replace("&","")
                notes = notes.replace("@","")
                notes = notes.replace("()","")
                notes = notes.replace("(","")
                notes = notes.replace(")","")
                notes = notes.replace("!","")
                notes = notes.replace("^","")
                notes = notes.replace("$","")
                notes = notes.replace("%","")
                notes = notes.replace("?","")
                notes = notes.replace("[]","")
                notes = notes.replace("{}","")


                audio_transcript = audio_transcription(notes)
                st.audio(audio_transcript)

        with st.container(border=True):
            st.subheader(f"🧪 Quiz - {difficulty} Level")

            with st.spinner("AI is creating quizzes..."):
                quiz = generate_quiz(pil_images, difficulty)

            st.markdown(quiz)

            st.download_button(
                label="⬇️ Download Quiz",
                data=quiz,
                file_name="generated_quiz.txt",
                mime="text/plain"
            )

    except Exception as error:
        st.error("Something went wrong while generating the result.")
        st.exception(error)



# import streamlit as st
# from api_calling import note_generator, audio_transcription, quiz_generator
# from PIL import Image    #gemini amra je image type dai ta text e convert korte pare na(means gemini tar file type er shathe match korte pare na), so we use pillow(pip list e ache, streamlit install dauar time e asheche) as PIL to convert this###

# #title
# st.title("📚 AI Study Assistant")
# st.write("Your smart learning companion")
# st.divider()

# with st.sidebar:    # with er help e ar por ja likbo shob sidebar e chole ashbe
#     st.header("Controls")

#     #image

#     images = st.file_uploader(
#         "Upload the photos of your note (Max 3)",
#         type=['jpg','jpeg','png'],
#         accept_multiple_files=True
#     )

#     pil_images = []

#     for img in images:
#         pil_img = Image.open(img)
#         pil_images.append(pil_img)

#     if images:
#         if len(images)>3:
#             st.error("Upload at max 3 images")
#         else:
#             col = st.columns(len(images))

#             st.subheader("Upload images")

#             for i,img in enumerate(images):
#                 with col[i]:
#                     st.image(img)

#     #difficulty
#     selected_option = st.selectbox(
#         "Enter the difficulty of your quiz",
#         ("Easy","Medium","Hard"),
#         index = None
#     )

#     pressed = st.button("Click the button to initiate AI", type='primary')

# if pressed:
#     if not images:
#         st.error("You must upload 1 image")
#     if not selected_option:
#         st.error("You must select a difficulty")

#     if images and selected_option:
        
#         #note

#         with st.container(border=True):
#             st.subheader("Your Note")

#             #the portion below will be replaced by API Call

#             with st.spinner("AI is writing notes for you"):
#                 generated_notes = note_generator(pil_images)
#                 st.markdown(generated_notes)

#         #Audio transcript

#         with st.container(border=True):
#             st.subheader("Audio Transcription")

#             #the portion below will be replaced by API Call
#             with st.spinner("AI is generating audio of this note"):

#                 #clearing the markdown

#                 generated_notes = generated_notes.replace("#","")
#                 generated_notes = generated_notes.replace("*","")
#                 generated_notes = generated_notes.replace("-","")
#                 generated_notes = generated_notes.replace("&","")
#                 generated_notes = generated_notes.replace("@","")


#                 audio_transcript = audio_transcription(generated_notes)
#                 st.audio(audio_transcript)
            
#         #quiz

#         with st.container(border=True):
#             st.subheader(f"Quiz ({selected_option}) Difficulty")

#             #the portion below will be replaced by API Call

#             with st.spinner("AI is generationg the quizzes"):
#                 quizzes = quiz_generator(pil_images, selected_option)
#                 st.markdown(quizzes)
            



# import streamlit as st
# from api_calling import note_generator, audio_transcription, quiz_generator
# from PIL import Image

# st.set_page_config(page_title="AI Study Assistant", layout="wide")

# # ---------------- Sidebar ----------------
# with st.sidebar:
#     st.title("📚 AI Study Assistant")
#     st.write("Your smart learning companion")

#     feature = st.radio("Choose Feature", [
#         "📝 Notes",
#         "🎧 Transcription",
#         "🧠 Quiz",
#         "📊 Performance"
#     ])

# # ---------------- Header ----------------
# st.title("📚 AI Study Assistant")
# st.markdown("Turn your study materials into notes, quizzes, and insights instantly.")
# st.divider()

# # ---------------- Notes Section ----------------
# if feature == "📝 Notes":
#     st.header("📝 Generate Notes from Image")

#     images = st.file_uploader(
#         "Upload Images (max 3)",
#         type=["png", "jpg", "jpeg"],
#         accept_multiple_files=True
#     )

#     if images:
#         if len(images) > 3:
#             st.error("⚠️ Upload maximum 3 images")
#         else:
#             cols = st.columns(len(images))
#             pil_images = []

#             for i, img in enumerate(images):
#                 pil_img = Image.open(img)
#                 pil_images.append(pil_img)

#                 with cols[i]:
#                     st.image(img, use_column_width=True)

#             if st.button("Generate Notes"):
#                 with st.spinner("Generating notes..."):
#                     try:
#                         notes = note_generator(pil_images)

#                         st.markdown("### 📒 Generated Notes")
#                         st.markdown(f"""
#                         <div style="background-color:#0b1c2d;padding:15px;border-radius:10px">
#                         {notes}
#                         </div>
#                         """, unsafe_allow_html=True)

#                         # Save for other sections
#                         st.session_state.notes = notes

#                     except Exception:
#                         st.error("⚠️ Failed to generate notes")

# # ---------------- Transcription Section ----------------
# elif feature == "🎧 Transcription":
#     st.header("🎧 Audio from Notes")

#     if "notes" not in st.session_state:
#         st.warning("⚠️ First generate notes from Images")
#     else:
#         if st.button("Generate Audio"):
#             with st.spinner("Generating audio..."):
#                 try:
#                     clean_text = st.session_state.notes
#                     for ch in ["#", "*", "-", "&", "@"]:
#                         clean_text = clean_text.replace(ch, "")

#                     audio = audio_transcription(clean_text)
#                     st.audio(audio)

#                 except Exception:
#                     st.error("⚠️ Failed to generate audio")

# # ---------------- Quiz Section ----------------
# elif feature == "🧠 Quiz":
#     st.header("🧠 Practice Quiz")

#     images = st.file_uploader(
#         "Upload Images for Quiz",
#         type=["png", "jpg", "jpeg"],
#         accept_multiple_files=True
#     )

#     difficulty = st.selectbox(
#         "Select Difficulty",
#         ["Easy", "Medium", "Hard"],
#         index=0
#     )

#     if images:
#         pil_images = [Image.open(img) for img in images]

#         if st.button("Generate Quiz"):
#             with st.spinner("Generating quiz..."):
#                 try:
#                     # ⚠️ send only ONE image (important fix)
#                     quiz = quiz_generator(pil_images[0], difficulty)
#                     st.markdown(quiz)

#                 except Exception:
#                     st.error("⚠️ AI server busy. Try again.")

# # ---------------- Performance Section ----------------
# elif feature == "📊 Performance":
#     st.header("📊 Your Performance")

#     if "score" not in st.session_state:
#         st.session_state.score = 0

#     st.metric("Quizzes Attempted", 0)
#     st.metric("Correct Answers", st.session_state.score)
#     st.metric("Accuracy", "Coming Soon")

#     st.progress(0)

# # ---------------- Footer ----------------
# st.markdown("---")
# st.markdown("Made with ❤️ using Streamlit & Gemini AI")
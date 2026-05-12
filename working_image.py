import streamlit as st
from PIL import Image
from api_calling import generate_notes


st.title("Image Test")

uploaded_images = st.file_uploader(
    "Upload images",
    type=["jpg", "jpeg", "png"],
    accept_multiple_files=True
)

if uploaded_images:
    pil_images = []

    for uploaded_file in uploaded_images:
        image = Image.open(uploaded_file).convert("RGB")
        pil_images.append(image)
        st.image(image, use_container_width=True)

    if st.button("Generate Notes"):
        notes = generate_notes(pil_images)
        st.markdown(notes)






# import streamlit as st

# from google import genai
# from dotenv import load_dotenv
# import os

# from PIL import Image


# #loading the environment variable
# load_dotenv()

# my_api_key = os.getenv("GEMINI_API_KEY")

# #initializing a client
# client = genai.Client(api_key= my_api_key)

# images = st.file_uploader(
#         "Upload the photos of your note",
#         type=['jpg','jpeg','png'],
#         accept_multiple_files=True
#     )


# if images:
    
#     pil_images = []

#     for img in images:
#         pil_img = Image.open(img)
#         pil_images.append(pil_img)


#     prompt = """Summarize the picture in note format at max 100 words
#     make sure to add necessary maarkdown to differentiate different section"""

#     response = client.models.generate_content(
#         model= "gemini-3-flash-preview",
#         contents=[pil_images, prompt]
#     )

#     st.markdown(response.text)
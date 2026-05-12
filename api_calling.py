from google import genai
from dotenv import load_dotenv
from gtts import gTTS
import os
import io
import re


load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found. Please add it inside your .env file.")

client = genai.Client(api_key=API_KEY)

MODEL_NAME = "gemini-3-flash-preview"


def generate_notes(images):
    if not images:
        raise ValueError("No images provided for note generation.")

    prompt = """
You are an academic study assistant.

Analyze the uploaded note images carefully and create a clean study note.

Requirements:
- Maximum 200 words
- Use clear Markdown formatting
- Use headings and bullet points
- Keep the language simple and student-friendly
- Focus only on important concepts
- Do not add unrelated information
- If the image is unclear, mention that clearly
"""

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=[prompt, *images]
    )

    if not response.text:
        raise ValueError("Gemini did not return any note content.")

    return response.text


def generate_quiz(images, difficulty):
    if not images:
        raise ValueError("No images provided for quiz generation.")

    prompt = f"Generator 5 quizzes based on the {difficulty}. Make sure to add markdown to differetiate the options. Add correct answer after the quiz."

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=[prompt, *images]
    )

    if not response.text:
        raise ValueError("Gemini did not return any quiz content.")

    return response.text


def audio_transcription(text):
    speech = gTTS(text, lang='en', slow=False)
    audio_buffer = io.BytesIO()
    speech.write_to_fp(audio_buffer)

    return audio_buffer





# from google import genai
# from dotenv import load_dotenv
# import os, io
# import time
# from gtts import gTTS


# #loading the environment variable
# load_dotenv()

# my_api_key = os.getenv("GEMINI_API_KEY")

# #initializing a client
# client = genai.Client(api_key= my_api_key)


# #note generator
# def note_generator(images):

#     prompt = """Summarize the picture in note format at max 100 words
#     make sure to add necessary maarkdown to differentiate different section"""

#     response = client.models.generate_content(
#         model= "gemini-3-flash-preview",
#         contents=[images, prompt]
#     )

#     return response.text


# #audio generator
# def audio_transcription(text):
#     speech = gTTS(text, lang='en', slow=False)
#     audio_buffer = io.BytesIO()
#     speech.write_to_fp(audio_buffer)

#     return audio_buffer

# #quiz generator
# def quiz_generator(image, difficulty):

#     prompt = f"Generator 3 quizzes based on the {difficulty}. Make sure to add markdown to differetiate the options. Add correct answer after the quiz."
#     # prompt = f"""
#     # Generate 3 multiple choice questions from the image with {difficulty} difficulty.

#     # Format STRICTLY like this:

#     # Q1: Question text
#     # A) Option 1
#     # B) Option 2
#     # C) Option 3
#     # D) Option 4
#     # Answer: A

#     # Q2: ...
#     # Answer: B

#     # Q3: ...
#     # Answer: C

#     # Do not add extra explanation.
#     # """

#     response = client.models.generate_content(
#         model= "gemini-3-flash-preview",
#         contents=[image, prompt]
#     )

#     return response.text



# prompt = f"""
# You are a quiz generator for students.

# Create quizzes from the uploaded note images.

# Requirements:
# - Difficulty level: {difficulty}
# - Create exactly 5 multiple-choice questions
# - Each question must have 4 options: A, B, C, D
# - Make sure to add markdown to differetiate the options.
# - Mark the correct answer after each question
# - Use clean Markdown formatting
# - Questions must be based only on the image content
# - Do not create questions from outside knowledge

# Format STRICTLY like this:
# ### Question 1
# Question text

# A. Option 1
# B. Option 2
# C. Option 3
# D. Option 4


# ✅ Correct Answer: B
# """
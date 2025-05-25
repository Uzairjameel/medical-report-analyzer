import streamlit as st
from dotenv import load_dotenv
import os
import google.generativeai as genai
from PIL import Image
import io

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("AIzaSyBc_yle3HMmQE7hMTKyD46n9AgjcgXd8eA"))

# Initialize the Gemini model
model = genai.GenerativeModel('gemini-1.5-flash')

st.title("Medical Report Analyzer with Gemini AI")
st.write("Upload your medical report or ask a question below:")

# File upload widget
uploaded_file = st.file_uploader("Choose a file", type=["jpg", "jpeg", "png", "pdf"])

# Text input for questions
user_input = st.text_input("Ask about your medical report:")

if uploaded_file is not None:
    st.write("File uploaded:", uploaded_file.name)

    # Read the image file
    file_bytes = uploaded_file.read()
    image = Image.open(io.BytesIO(file_bytes))
    st.image(image, caption="Uploaded Image", use_column_width=True)

if user_input:
    if uploaded_file:
        # Pass the image and user question directly to Gemini API
        response = model.generate_content([user_input, image])
        st.write("AI Response:", response.text)
    else:
        response = model.generate_content(user_input)
        st.write("AI Response:", response.text)
from dotenv import load_dotenv
load_dotenv() #loading all the environment variables

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#Function to load Gemini Pro Vision model and get response

model = genai.GenerativeModel("gemini-pro-vision")
def get_gemini_response(input, image):
    if input != "":
        response = model.generate_content([input, image])

    else:
        response = model.generate_content(image)
    
    return response.text


# Initializing Streamlit Application

st.set_page_config(page_title="Gemini Image Application")

st.header("Gemini Application")
input = st.text_input("input Prompt: ", key="input")

# File Uploading setup

uploaded_file = st.file_uploader("Choose an image....", type=["jpg","jpeg","png"])
image = ""

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image...", use_column_width=True)

submit = st.button("Tell me about the Image")

# If Submit is Clicked

if submit:
    response = get_gemini_response(input,image)
    st.subheader("The Response is")
    st.write(response)

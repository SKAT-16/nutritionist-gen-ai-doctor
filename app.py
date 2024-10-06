from dotenv import load_dotenv
import os
import streamlit as st
import google.generativeai as genai
from PIL import Image

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel(model_name="gemini-1.5-flash")


def get_gemini_response(input, image, prompt):
    response = model.generate_content([input, image[0], prompt])
    return response.text


def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = [{"mime_type": uploaded_file.type, "data": bytes_data}]

        return image_parts
    else:
        raise FileNotFoundError("No file uploaded!")


st.set_page_config(
    page_title="Nutritionist Generative AI Doctor", page_icon="📝", layout="wide"
)
st.header("Gemini AI Doctor")
input = st.text_input("Input: ", key="input")
uploaded_file = st.file_uploader(
    "Choose an image of your daily food...", type=["jpg", "jpeg", "png"]
)
image = ""

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Invoice", use_column_width=True)

submit = st.button("Tell me about the food")
input_prompt = """You are a Nutritionist Generative AI Doctor. You will analyze the provided image of a food item or meal, 
                  and summarize its nutritional content and health benefits. Please provide the important information 
                  and dietary advice in points within 250 words. The food item is: """

if submit:
    image_data = input_image_setup(uploaded_file)
    response = get_gemini_response(input, image_data, input_prompt)
    st.subheader("The Response is")
    st.write(response)

import streamlit as st
import os
from dotenv import load_dotenv
import openai
import torch
from diffusers import StableDiffusionPipeline
from midjourney_api import TNL
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
TNL_API_KEY = os.getenv("TNL_API_KEY")

#function to generate image using DALL-E
def dall_e(prompt):
    response = openai.Image.create(
        prompt=input_text,
        n=1,
        size='512x512',
    )
    image_url= response['data'][0]['url']
    # image_url= response['data']
    return image_url

#function to generate image using Diffusion
def diffusion(input_text):
    pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5",torch_device="cuda")
    pipe=pipe.to("cuda")
    image=pipe(input_text).image[0]
    return image


choice=st.sidebar.selectbox("Select the choice",["Home","DALL-E","Diffusion"])

if choice=="Home":
    st.title("AI Image Generation App")
    st.subheader("Select the choice from the sidebar")

elif choice=="DALL-E":
    st.title("AI Image Generation Using DALL-E")
    input_text=st.text_input("Enter the Prompt")
    if input_text is not None:
        if st.button("Generate Image"):
            st.spinner("Generating Image")
            image_url=dall_e(input_text)
            # st.write(image_url)
            st.image(image_url,use_column_width=True,caption="Generated Image")


elif choice=="Diffusion":
    st.title("AI Image Generation Using Diffusion")
    st.subheader("AI Image Generation using Diffusion")
    input_text=st.text_input("Enter the Prompt")
    if input_text is not None:
        if st.button("Generate Image"):
            st.spinner("Generating Image")
            image_url=diffusion(input_text)
            # st.write(image_url)
            st.image(image_url,use_column_width=True,caption="Generated Image using Hugging Face Diffusion")

            
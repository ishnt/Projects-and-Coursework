
import streamlit as st
from diffusers import DiffusionPipeline
import torch
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
# Function to generate image based on prompt
def generate_image(prompt):
    pipe = DiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-xl-base-1.0", torch_dtype=torch.float16, use_safetensors=True, variant="fp16")
    pipe.to("cuda")
    # In a real scenario, this function would call your image generation model
    # and return the generated image.
    # For this example, let's just return a placeholder image.
    images = pipe(prompt=prompt).images[0]
    return images

# Streamlit UI
def main():
    
    st.title("Image Generator")

    # User prompt input
    prompt = st.text_input("Enter your prompt:", "A beautiful landscape with mountains")

    # Generate image button
    if st.button("Generate Image"):
        # Generate the image based on the prompt
        image = generate_image(prompt)
        
        # Display the generated image
        st.image(image, caption='Generated Image', use_column_width=True)

if __name__ == "__main__":
    main()

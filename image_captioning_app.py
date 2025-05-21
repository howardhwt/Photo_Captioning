import gradio as gr
import numpy as np
from PIL import Image
from transformers import AutoProcessor, BlipForConditionalGeneration

base = "Salesforce/blip-image-captioning-base"
processor = AutoProcessor.from_pretrained(base)
model = BlipForConditionalGeneration.from_pretrained(base)

def caption_image(input_image: np.ndarray):
    # Convert numpy array to PIL Image and convert to RGB
    raw_image = Image.fromarray(input_image).convert('RGB')
    
    # Process the image
    

    # Generate a caption for the image


    # Decode the generated tokens to text and store it into `caption`
    

    return caption
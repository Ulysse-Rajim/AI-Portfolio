import streamlit as st
import os
from PIL import Image

def show():
    st.subheader("Image Gallery")
    st.write('Here are some of my AI projects TEST.')

    # Set the directory where your images are stored
    image_dir = "./images/"
    
    # List all the image files in the directory
    image_files = [file for file in os.listdir(image_dir) if file.endswith(('png', 'jpg', 'jpeg'))]
    
    # Set the number of columns for your gallery
    columns = 3
    col_index = 0
    cols = st.columns(columns)
    
    # Loop through the image files and place them in columns
    for i, image_file in enumerate(image_files):
        with cols[col_index]:
            image = Image.open(os.path.join(image_dir, image_file))
            st.image(image, use_column_width=True)
        
        # Update the column index
        col_index = (col_index + 1) % columns

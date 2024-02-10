# home.py

import streamlit as st

def show():
    st.subheader("Welcome to My AI Portfolio")
    st.write("This is the home page of my AI Portfolio.")
    
    # Introduction section
    st.write("""
        Hi, I'm [Your Name]! I'm an AI practitioner with a love for turning complex 
        data into actionable insights. I have a background in [Your Background], and 
        I've worked on projects involving [List a Few Types of Projects].
    """)
    
    # Skills section
    st.subheader("Skills")
    st.write("""
        - Machine Learning
        - Data Analysis
        - Natural Language Processing
        - Computer Vision
        - Deep Learning Frameworks (TensorFlow, PyTorch)
    """)
    
    # You can continue adding more sections like 'Experience', 'Education', etc.

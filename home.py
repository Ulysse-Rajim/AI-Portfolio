# home.py

import streamlit as st

def show():
    st.subheader("Welcome to My AI Portfolio")
    st.write("This is the home page of my AI Portfolio.")
    
    # Introduction section
    st.write("""
        Hi, I'm Ulysse! I'm an AI engineer with a love for exploring new AI technologies. I have a background in Telecommunications and computer science, and 
        I've worked on projects involving LLMs, RAG architectures,...
    """)
    
    # Skills section
    st.subheader("Skills")
    st.write("""
        - Deep Learning
        - LLMs
        - Computer Vision
    """)
    
    # You can continue adding more sections like 'Experience', 'Education', etc.

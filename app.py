import streamlit as st
#from pages import callbot, chatbot

# Define the pages
#PAGES = {
#    #"Home": home,
#    #"Projects": projects,
#    "Chatbot": chatbot,
#    "Callbot": callbot,
#}

def main():
    st.set_page_config(
        page_title="AI Portfolio",
        page_icon="🤖",
        layout="wide",
        )
    
    #st.title("AI Portfolio")
    st.sidebar.success("Select a demo above")
    
    # Load the custom CSS
    with open('styles/style.css', 'r') as f:
        css = f.read()
    st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)


    # Streamlit app code
    create_header("My AI Portfolio")

    # Navigation
    #st.sidebar.title("Navigation")
    #selection = st.sidebar.radio("Go to", list(PAGES.keys()))

    # Page Display
    #page = PAGES[selection]
    #page.show()

    create_footer()

def create_header(title):
    st.markdown(
        f"""
        <div class="header" id="custom-header">
            <h1>{title}</h1>
        </div>
        """,
        unsafe_allow_html=True,
    )

def create_footer():
    st.markdown(
        """
        <div class="footer" id="custom-footer">
            <p>Designed by Ulysse Rajim | © 2024 All rights reserved</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

if __name__ == "__main__":
    main()

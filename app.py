import streamlit as st
from PIL import Image

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="HEARTS_BLOG", page_icon=":heart:", layout="wide")

# Define your background image URL from GitHub repository (use the direct link to the raw image file)
background_image_url = "https://raw.githubusercontent.com/Shenheart/MYWEB/main/PIC.jpg"

# Apply the background image using custom CSS
background_style = f"""
    <style>
        .stApp {{
            background-image: url('{background_image_url}');
            background-size: cover;
            background-repeat: no-repeat;
        }}
        .css-17eq0hr, .css-1v1k8g1, .css-1be9khp {{
            color: black !important;
        }}
    </style>
"""
st.markdown(background_style, unsafe_allow_html=True)

img = Image.open("Me.jpg")
st.image(img, width=600, channels="RGB")


st.title("Hi, I'm Shen Heart Glico and Welcome To my Blog :wave:, \n where you'll learn more about me")
st.header("I'm a 1st Year College Student in BSCPE Course")
st.write("I'm learning how to code and program")
st.write("Message me on Facebook [Click here >](https://www.facebook.com/sikuansecret.07")

st.write("---")
st.header("About me:")
st.write("##")
st.write(
    """
    -
    """
)

st.image("https://raw.githubusercontent.com/YourGitHubUsername/YourRepositoryName/main/path/to/your/background_image.jpg", use_column_width=True)

import streamlit as st
from multipage import MultiPage
from pages import page1, page2, page3  # Import your app modules here

# Create an instance of the app
app = MultiPage()

# Title of the main page
st.title("Dummy Multipage Streamlit App")

# Add all your applications (pages) here
app.add_page("Page 1", page1.app)
app.add_page("Page 2", page2.app)
app.add_page("Page 3", page3.app)

# The main app
app.run()
# import streamlit as st
# from multipage import MultiPage
# from pages import page1, page2, page3  # Import your app modules here

# # Create an instance of the app
# app = MultiPage()

# # Title of the main page
# st.title("Dummy Multipage Streamlit App")

# # Add all your applications (pages) here
# app.add_page("XPage 1", page1.app)
# app.add_page("XPage 2", page2.app)
# app.add_page("XPage 3", page3.app)

# # The main app
# app.run()


import streamlit as st

# Function to manage page navigation
def navigate_to(page):
    st.experimental_set_query_params(page=page)

# Function to render page content
def render_page(page):
    if page == "page1":
        st.title("Page 1")
        st.write("Welcome to Page 1!")
        st.markdown("[Go to Home](?page=home)")
        st.markdown("[Go to Page 2](?page=page2)")

    elif page == "page2":
        st.title("Page 2")
        st.write("Welcome to Page 2!")
        st.markdown("[Go to Home](?page=home)")
        st.markdown("[Go to Page 1](?page=page1)")

    else:
        st.title("Home")
        st.write("Welcome to the Home Page!")
        st.markdown("[Go to Page 1](?page=page1)")
        st.markdown("[Go to Page 2](?page=page2)")

# Main function
def main():
    st.write("Starting the app...")  # Debugging line to check if the app runs
    query_params = st.experimental_get_query_params()
    st.write(f"Query parameters: {query_params}")  # Debugging line to see the query parameters
    page = query_params.get("page", ["home"])[0]
    
    st.write(f"Rendering page: {page}")  # Debugging line to confirm the correct page is selected
    render_page(page)

if __name__ == "__main__":
    main()

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
    st.query_params(page=page)

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
    st.sidebar.title("Credentials")

    # Option 1
    # if 'credentials' not in st.session_state:
    #     # Input fields for credentials
    #     username = st.sidebar.text_input("Enter Username")
    #     password = st.sidebar.text_input("Enter Password", type="password")

    #     if st.sidebar.button("Save Credentials"):
    #         st.session_state['credentials'] = f"{username} (password: {password})"
    #         st.sidebar.success("Credentials saved!")
    # else:
    #     st.sidebar.success("Credentials already saved!")

    # if st.sidebar.button("Show session state"):
    #     st.write("Current session state:")
    #     st.write(st.session_state)

    # Option 2

    # Header for the sidebar
    # st.sidebar.header("API Key & Value Storage")

    # # Check if the values are already set in session state
    # if "stored_api_key" not in st.session_state or "stored_api_value" not in st.session_state:
    #     # Display input fields if values are not set
    #     api_key = st.sidebar.text_input("API Key", "")
    #     api_value = st.sidebar.text_input("API Value", "")

    #     if st.sidebar.button("Save"):
    #         if api_key and api_value:
    #             # Save the key and value to session state
    #             st.session_state.stored_api_key = api_key
    #             st.session_state.stored_api_value = api_value
    #             st.sidebar.success("Key and Value have been saved!")
    #         else:
    #             st.sidebar.error("Please enter both key and value.")

    # else:
    #     # Show message and update button if values are already set
    #     st.sidebar.write("API Key and Value are already set.")
    #     st.sidebar.write(f"Stored API Key: {st.session_state.stored_api_key}")
    #     st.sidebar.write(f"Stored API Value: {st.session_state.stored_api_value}")
        
    #     if st.sidebar.button("Update Key & Value"):
    #         # Clear the session state to allow for updating
    #         del st.session_state.stored_api_key
    #         del st.session_state.stored_api_value
    #         st.sidebar.success("You can now enter new key and value.")


    # Option 3
    # Header for the sidebar
    st.sidebar.header("API Key & Value Storage")

    # Initialize session state variables if they don't exist
    if "stored_api_key" not in st.session_state:
        st.session_state.stored_api_key = None
    if "stored_api_value" not in st.session_state:
        st.session_state.stored_api_value = None
    if "show_inputs" not in st.session_state:
        st.session_state.show_inputs = True

    # Function to handle saving the API key and value
    def save_credentials():
        if st.session_state.api_key and st.session_state.api_value:
            st.session_state.stored_api_key = st.session_state.api_key
            st.session_state.stored_api_value = st.session_state.api_value
            st.session_state.show_inputs = False
            st.session_state.api_key = ""  # Clear input fields
            st.session_state.api_value = ""  # Clear input fields
            st.sidebar.success("Key and Value have been saved!")
        else:
            st.sidebar.error("Please enter both key and value.")

    # Display input fields if they are not yet set
    if st.session_state.show_inputs:
        # Define text input fields using session state keys
        st.sidebar.text_input("API Key", key="api_key")
        st.sidebar.text_input("API Value", key="api_value")
        if st.sidebar.button("Save"):
            save_credentials()
    else:
        # Show stored values and update button if inputs are not shown
        st.sidebar.write("API Key and Value are already set.")
        st.sidebar.write(f"Stored API Key: {st.session_state.stored_api_key}")
        st.sidebar.write(f"Stored API Value: {st.session_state.stored_api_value}")
        
        if st.sidebar.button("Update Key & Value"):
            # Allow updating by showing input fields again
            st.session_state.show_inputs = True
            st.session_state.api_key = ""  # Reset input fields
            st.session_state.api_value = ""  # Reset input fields
            st.sidebar.success("You can now enter new key and value.")



    #st.write("Starting the app...")  # Debugging line to check if the app runs
    query_params = st.experimental_get_query_params()
    #st.write(f"Query parameters: {query_params}")  # Debugging line to see the query parameters
    page = query_params.get("page", ["home"])[0]
    
    #st.write(f"Rendering page: {page}")  # Debugging line to confirm the correct page is selected
    render_page(page)

if __name__ == "__main__":
    main()

import streamlit as st
from PIL import Image
from config.config import load_config
from page.about_us import display_about_us
from page.home import display_home
from page.data_exploration import display_data_exploration

load_config()

# Set page configuration as the first command
st.set_page_config(
    page_title="Journify",
    page_icon=":shield:",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.sidebar.image("Journify/resource/journify_logo.png")
st.sidebar.header("How to use Journify")

# ------------------ MultiApp Structure with Sidebar Buttons ------------------ #
class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({"title": title, "function": func})

    def run(self):
        # Sidebar menu for each added app
        st.sidebar.markdown("## Main Menu")
        selected_app = None
        
        # Display each app title as a button in the sidebar
        for app in self.apps:
            if st.sidebar.button(app["title"]):
                selected_app = app["function"]

        st.sidebar.markdown("---")

        # Display the selected app function (if any)
        if selected_app:
            selected_app()
        else:
            st.write("Select a page from the sidebar.")

# Initialize the MultiApp instance
app = MultiApp()

# Add pages as individual apps
app.add_app("Home Page", display_home)
app.add_app("Database Overview", display_data_exploration)
app.add_app("Search PDB", display_data_exploration)  # Replace with actual function
app.add_app("Explore Conformations", display_data_exploration)  # Replace with actual function
app.add_app("Analyze Mutations", display_data_exploration)  # Replace with actual function
app.add_app("Compare Inhibitors", display_data_exploration)  # Replace with actual function
app.add_app("Query Database", display_data_exploration)  # Replace with actual function
app.add_app("Classify Structures", display_data_exploration)  # Replace with actual function
app.add_app("About Us", display_about_us)

# Run the app
app.run()

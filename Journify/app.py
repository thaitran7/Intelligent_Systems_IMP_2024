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

# ------------------ MultiApp Structure with Selectbox and Markdown ------------------ #
class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({"title": title, "function": func})

    def run(self):
        # Display the main menu with markdown and a selectbox for navigation
        st.sidebar.markdown("## Main Menu")
        
        # Use selectbox to allow the user to choose an app
        app = st.sidebar.selectbox(
            "Select Page", self.apps, format_func=lambda app: app["title"]
        )
        
        st.sidebar.markdown("---")  # Divider line

        # Display the selected app function
        app["function"]()

# Initialize the MultiApp instance
app = MultiApp()

# Add each page to the app
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

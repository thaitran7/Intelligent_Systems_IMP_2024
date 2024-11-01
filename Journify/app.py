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
st.sidebar.header("About")

# Sidebar content with some information about Journify
with st.sidebar:
    st.markdown("Welcome to **Journify** (Intelligent Journal Explorer), an AI-powered platform designed to provide users with curated article recommendations and an intelligent Q&A chatbot for arXiv papers.")
    st.markdown("Created by the Journify Team.")
    st.sidebar.markdown("⭐ Star on GitHub: [![Star on GitHub](https://img.shields.io/github/stars/tan-nt/real-life-streamlit-app?style=social)](https://github.com/tan-nt/real-life-streamlit-app)")
    st.markdown("""---""")

# FAQ section in the sidebar
st.sidebar.header("FAQs")
with st.sidebar:
    st.markdown(
        """
    ### **What is Journify?**
    Journify is an intelligent journal exploration tool designed to recommend the best articles and answer queries from arXiv using AI.
    """
    )

# ------------------ MultiApp Structure with Tabs ------------------ #
class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({"title": title, "function": func})

    def run(self):
        # Create a list of tab names from added apps
        tab_titles = [app["title"] for app in self.apps]
        # Create tabs using Streamlit's st.tabs
        tabs = st.tabs(tab_titles)
        
        # Display each app's function in the corresponding tab
        for i, app in enumerate(self.apps):
            with tabs[i]:
                app["function"]()

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

# Run the app to display tabs
app.run()

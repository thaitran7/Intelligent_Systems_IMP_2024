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

# ------------------ Main App UI ------------------ #
class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({"title": title, "function": func})

    def run(self):
        # Sidebar for selecting the app
        st.sidebar.markdown("## Main Menu")
        
        # Selectbox for navigation
        app = st.sidebar.selectbox(
            "Select Page", self.apps, format_func=lambda app: app["title"]
        )
        st.sidebar.markdown("---")
        
        # Display the selected page content
        app["function"]()

# Initialize and add pages
app = MultiApp()
app.add_app("Home Page", display_home)
app.add_app("Database Overview", display_data_exploration)
app.add_app("Search PDB", display_data_exploration)  # Replace with actual function
app.add_app("Explore Conformations", display_data_exploration)  # Replace with actual function
app.add_app("Analyze Mutations", display_data_exploration)  # Replace with actual function
app.add_app("Compare Inhibitors", display_data_exploration)  # Replace with actual function
app.add_app("Query Database", display_data_exploration)  # Replace with actual function
app.add_app("Classify Structures", display_data_exploration)  # Replace with actual function
app.add_app("About Us", display_about_us)

# Run the application
app.run()

st.sidebar.markdown("---")

# Display a smaller logo with a width setting
st.sidebar.image("Journify/resource/journify_logo.png", width=150)

# Brief, engaging description
st.sidebar.markdown(
    """
    **Welcome to Journify**, your intelligent journal explorer powered by AI. Journify is crafted to 
    empower researchers, students, and curious minds by providing:
    - **Curated article recommendations** for deep insights across a range of topics.
    - An **AI-driven Q&A chatbot** designed to answer your research questions quickly and accurately.
    """
)

st.sidebar.markdown("---")

st.sidebar.markdown(
    """
    Join us in turning learning into growth and unlock new possibilities with **Journify**.
    """
)

# Add a call to action for engagement
st.sidebar.markdown("#### ⭐ Explore, Learn, and Grow with Journify!")
st.sidebar.markdown(
    "Support us by starring on GitHub: "
    "[![Star on GitHub](https://img.shields.io/github/stars/tan-nt/real-life-streamlit-app?style=social)]"
    "(https://github.com/tan-nt/real-life-streamlit-app)"
)



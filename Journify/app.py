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
        st.sidebar.markdown("<h2 style='text-align: center;'>Main Menu</h2>", unsafe_allow_html=True)
        
        # Selectbox for navigation with a centered title
        app = st.sidebar.selectbox(
            "Select Page", self.apps, format_func=lambda app: app["title"]
        )
        st.sidebar.markdown("<hr style='border: 1px solid #d3d3d3;'>", unsafe_allow_html=True)
        
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

# Display a centered and smaller logo
st.sidebar.markdown(
    "<div style='text-align: center;'>"
    "<img src='Journify/resource/journify_logo.png' width='120' alt='Journify Logo'>"
    "</div>",
    unsafe_allow_html=True
)

# Add a brief, engaging description with interactive styles
st.sidebar.markdown(
    """
    <div style="padding: 15px; text-align: center; border-radius: 10px; background-color: #f0f0f0;">
    <strong>Welcome to Journify</strong>, your intelligent journal explorer powered by AI.<br><br>
    Journify empowers researchers, students, and curious minds by providing:<br>
    <ul style="text-align: left;">
        <li>Curated article recommendations for deep insights across topics.</li>
        <li>An AI-driven Q&A chatbot to answer research questions quickly.</li>
    </ul>
    </div>
    """,
    unsafe_allow_html=True
)

# Add a motivational call-to-action and slogan
st.sidebar.markdown(
    """
    <div style="text-align: center; margin-top: 20px; font-size: 1.2em; font-weight: bold;">
    ⭐ Explore, Learn, and Grow with Journify!
    </div>
    """
)

# Call-to-action to support Journify on GitHub with a clickable button
st.sidebar.markdown(
    """
    <div style="text-align: center; margin-top: 20px;">
    <a href="https://github.com/tan-nt/real-life-streamlit-app" target="_blank">
        <button style="background-color: #ff4b4b; color: white; border: none; padding: 10px 20px; border-radius: 5px; font-size: 1em;">
            Star on GitHub
        </button>
    </a>
    </div>
    """,
    unsafe_allow_html=True
)

# Separator line for structure
st.sidebar.markdown("<hr style='border: 1px solid #d3d3d3;'>", unsafe_allow_html=True)

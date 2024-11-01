import base64
import streamlit as st
from PIL import Image
from config.config import load_config
from pages.search_page import search_page
from pages.about_us_page import about_us_page
from pages.home_page import home_page
from pages.trendings_page import trendings_page

# Set page configuration as the first command
st.set_page_config(
    page_title="Journify",
    page_icon=":shield:",
    layout="wide",
    initial_sidebar_state="expanded"
)

load_config()

# Function to encode images to base64
def load_image(image_file):
    try:
        with open(image_file, "rb") as file:
            return base64.b64encode(file.read()).decode()
    except Exception as e:
        st.error(f"Error loading image: {e}")
        return None

# Load images
journify_logo = load_image("Journify/resource/journify_logo.png")

# ------------------ Main App UI ------------------ #
class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({"title": title, "function": func})

    def run(self):
        
        # Selectbox for navigation
        app = st.sidebar.selectbox(
            "Select Page", self.apps, format_func=lambda app: app["title"]
        )
        st.sidebar.markdown("---")
        
        # Display the selected page content
        app["function"]()

# Initialize and add pages
app = MultiApp()
app.add_app("Home Page", home_page)
app.add_app("Search Articles", search_page)
app.add_app("Chat Bot", trendings_page)  # Replace with actual function
app.add_app("Journal Suggester", search_page)  # Replace with actual function
app.add_app("Research Trendings", search_page)  # Replace with actual function
app.add_app("About us", about_us_page)  # Replace with actual function

# Run the application
app.run()

# Centered Logo and Additional Sidebar Content
if journify_logo is None:
    st.error("Logo file not found!")
else:
    st.sidebar.markdown(
        """
        <div style="display: flex; justify-content: center; gap: 20px; margin: 10px 0;">
            <img src="data:image/png;base64,{journify_logo}" alt="Intelligent Article Explorer Logo" width="200">
        </div>
        """.format(journify_logo=journify_logo), 
        unsafe_allow_html=True
    )

# Brief, engaging description with emojis and enhanced formatting
st.sidebar.markdown(
    """
    <div style='text-align: center;'>
    <h1>🌱 Welcome to Journify 🌱</h1>
    <div>
    """, unsafe_allow_html=True
)
st.sidebar.markdown(
    """
    <div style='text-align: justify;'>
    Your intelligent journal explorer powered by AI. Journify empowers scholars and curious minds by providing:
    <ul>
        <li>🔍 <strong>Curated Article Recommendations</strong> across a wide range of topics.</li>
        <li>🤖 <strong>AI-driven Q&A Chatbot</strong> for quick, accurate answers to your research questions.</li>
    </ul>
    </div>
    """, unsafe_allow_html=True
)

st.sidebar.markdown("---")

# Vision and Mission Statement
st.sidebar.markdown(
    """
    <div style='text-align: center;'>
    <h2>🚀 Transforming Learning into Lifelong Growth 🚀</h2>
    <strong>Journify</strong> is to support your journey toward academic excellence.<br> 
    <em>Join us in unlocking new possibilities through knowledge and innovation.</em>
    </div>
    """, unsafe_allow_html=True
)

st.sidebar.markdown("---")

st.sidebar.markdown(
    """
    <div style='text-align: center;'>
        <h3>⭐ Explore, Learn, and Grow with Journify! ⭐</h3>
    </div>
    """, unsafe_allow_html=True
)

st.sidebar.markdown(
    """
    <div style='text-align: center;'>
        <a href="https://github.com/tan-nt/real-life-streamlit-app">
            <img src="https://img.shields.io/github/stars/tan-nt/real-life-streamlit-app?style=social" alt="Star on GitHub">
        </a>
    </div>
    """, unsafe_allow_html=True
)

st.sidebar.markdown("---")

# FAQ Section with collapsible details for interactivity
st.sidebar.header("FAQs")
with st.sidebar.expander("What is Journify?"):
    st.write("Journify is a platform that leverages AI to recommend articles and answer research questions, providing you with an academic companion for discovery and insight.")

with st.sidebar.expander("How does Journify work?"):
    st.write("Using advanced algorithms such as KNN classification, Bayesian search, and recommendation models, Journify personalizes high-accuracy content based on your research needs.")

with st.sidebar.expander("Is my data stored?"):
    st.write("No, all queries are processed in real-time and deleted at the session's end to ensure privacy.")

with st.sidebar.expander("Why might responses take some time?"):
    st.write("Complex queries require additional processing time. Free-tier users may experience some delay due to system limits.")

st.sidebar.markdown("---")
st.sidebar.markdown("📘 **Tips for Best Results**: Provide detailed questions for more accurate recommendations and improved insights.")

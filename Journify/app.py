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

# Centered Logo and Additional Sidebar Content
st.sidebar.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
st.sidebar.image("Journify/resource/journify_logo.png", width=120)
st.sidebar.markdown("</div>", unsafe_allow_html=True)

# Brief, engaging description with emojis and enhanced formatting
st.sidebar.markdown(
    """
    <div style='text-align: center;'>
    <strong>🌱 Welcome to Journify 🌱</strong>
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
    🚀 <strong>Transforming Learning into Lifelong Growth</strong><br>
    <strong>Journify<strong> is to support your journey toward academic excellence.<br> 
    <em>Join us in unlocking new possibilities through knowledge and innovation.</em>
    </div>
    """, unsafe_allow_html=True
)

st.sidebar.markdown(
    """
    <div style='text-align: center;'>
        <strong>⭐ Explore, Learn, and Grow with Journify!</strong>
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

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

# Display a smaller logo with a width setting
st.sidebar.image("Journify/resource/journify_logo.png", width=150)

# Add an appealing title and slogan
st.sidebar.title("Journify")
st.sidebar.markdown("### Transforming Learning into Lifelong Growth")

# Brief, engaging description
st.sidebar.markdown(
    """
    **Welcome to Journify**, your intelligent journal explorer powered by AI. Journify is crafted to 
    empower researchers, students, and curious minds by providing:
    - **Curated article recommendations** for deep insights across a range of topics.
    - An **AI-driven Q&A chatbot** designed to answer your research questions quickly and accurately.
    
    Explore the power of AI in academic research with our **state-of-the-art technology**:
    - **K-Nearest Neighbors (KNN)** for efficient subject classification.
    - **Bayesian Search** for refined, intelligent querying.
    - **High-accuracy recommendation engines** using **HNSW-ANN** and **BERT (Weaviate)**.
    - **Large Language Model (LLM) + RAG Chatbot** for responsive and reliable answers.
    
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

# Separator line for structure
st.sidebar.markdown("---")

# Frequently Asked Questions (FAQ) Section
st.sidebar.header("FAQs")
st.sidebar.markdown(
    """
    **What is Journify?**  
    Journify is a platform that leverages AI to recommend articles and answer research questions. It's your academic companion for discovery and insight.
    
    **How does Journify work?**  
    With KNN classification, Bayesian search, and recommendation models, Journify brings you personalized, high-accuracy content.

    **Is my data stored?**  
    No, all queries are temporary and deleted at the session's end.
    
    **Why can it take time to generate responses?**  
    Complex queries may require additional processing. Free-tier users may experience some delay due to system limits.
    
    **Tips for best results:**  
    Provide detailed questions with clear topics for more accurate recommendations.
    """
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

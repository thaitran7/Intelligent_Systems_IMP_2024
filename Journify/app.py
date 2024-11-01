import streamlit as st
from PIL import Image

from util.functions.path import get_file_path, get_dir_name, util_str, data_str
from util.pages.home_page import home_page
from util.pages.overview_page import overview_page
from util.pages.pdb_page import pdb_page
from util.pages.conformation_page import conformation_page
from util.pages.mutation_page import mutation_page
from util.pages.inhibitor_page import inhibitor_page
from util.pages.query_page import query_page
from util.pages.classify_page import classify_page

# Custom CSS for better visuals
st.markdown(
    """
    <style>
    .main {
        background-color: #f9f9f9;  /* Light background */
    }
    .tab-title {
        font-size: 24px;  /* Bigger tab font size */
        font-weight: bold;
        color: #4CAF50; /* Green color for tab titles */
    }
    </style>
    """,
    unsafe_allow_html=True
)

class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({"title": title, "function": func})

    def run(self):
        img = Image.open(
            get_file_path(
                "rascore_logo.png",
                dir_path=f"{get_dir_name(__file__)}/{util_str}/{data_str}",
            ),
        )

        st.set_page_config(page_title="rascore", page_icon=img, layout="wide")

        # Display a logo at the top of the page
        st.image(img, width=200)

        # Creating tabs for navigation
        tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(
            ["Home", "Database Overview", "Search PDB", "Explore Conformations", 
             "Analyze Mutations", "Compare Inhibitors", "Query Database"]
        )

        with tab1:
            home_page()  # Display home page
        with tab2:
            overview_page()  # Display database overview
        with tab3:
            pdb_page()  # Display search PDB page
        with tab4:
            conformation_page()  # Display explore conformations page
        with tab5:
            mutation_page()  # Display analyze mutations page
        with tab6:
            inhibitor_page()  # Display compare inhibitors page
        with tab7:
            query_page()  # Display query database page

# Create a MultiApp instance and add apps
app = MultiApp()
app.run()

# ---- Additional Features for Journify ---- #
# Set up the Journify application
load_config()

# Set page configuration as the first command
st.set_page_config(
    page_title="Journify",
    page_icon=":shield:",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.sidebar.image("Journify/resource/journify.png")
st.sidebar.header("How to use Journify")

st.sidebar.header("About")
with st.sidebar:
    st.markdown(
        "Welcome to **Journify** (Intelligent Journal Explorer), an AI-powered platform designed to provide users with curated article recommendations and an intelligent Q&A chatbot for arXiv papers."
    )
    st.markdown(
        """
        Journify leverages advanced AI models to deliver relevant content and insights. Our platform combines multiple state-of-the-art techniques, such as:
        - **KNN** for subject classification and filtering.
        - **Bayesian Search** for intelligent querying.
        - **HNSW-ANN and BERT (Weaviate)** for high-accuracy recommendation systems.
        - **LLM + RAG** for Q&A with our chatbot, providing quick, reliable answers to your research questions.
        """
    )
    st.markdown("Created by the Journify Team.")
    
    # Add "Star on GitHub" link to the sidebar
    st.sidebar.markdown(
        "⭐ Star on GitHub: [![Star on GitHub](https://img.shields.io/github/stars/tan-nt/real-life-streamlit-app?style=social)](https://github.com/tan-nt/real-life-streamlit-app)"
    )
    st.markdown("""---""")

# Add "FAQs" section to the sidebar
st.sidebar.header("FAQs")
with st.sidebar:
    st.markdown(
        """
    ### **What is Journify?**
    Journify is an intelligent journal exploration tool designed to recommend the best articles and answer queries from arXiv using AI. It combines various machine learning techniques to provide relevant, curated content and a seamless research experience.
    """
    )
    st.markdown(
        """
    ### **How does Journify work?**
    Journify utilizes a combination of KNN for classification, Bayesian methods for search, HNSW-ANN and BERT (via Weaviate) for recommendations, and an LLM + RAG-based chatbot to deliver efficient and accurate recommendations and insights.
    """
    )
    st.markdown(
        """
    ### **Do you store the queries or recommendations?**
    No, Journify does not store any personal data or queries. All interactions are temporary and are cleared after the session ends.
    """
    )
    st.markdown(
        """
    ### **Why does it take time to generate recommendations or answer queries?**
    Processing can vary based on query complexity and system load. Free users may experience slower response times due to rate limits. Consider using a paid tier for faster responses.
    """
    )
    st.markdown(
        """
    ### **Are recommendations and answers always accurate?**
    While Journify uses advanced models, results may not be 100% accurate. Machine learning models like BERT and LLMs can sometimes misinterpret or 'hallucinate' content. We recommend using Journify's output as a guide and verifying with additional sources if needed.
    """
    )
    st.markdown(
        """
    ### **How can I get the best recommendations and answers?**
    Provide detailed queries and specify topics clearly. The more context you give, the more relevant and accurate the recommendations and responses from Journify will be.
    """
    )

# ------------------ Main App UI ------------------ #
tab1, tab2, tab3, tab4 = st.tabs(["Home", "Article Recommendation", "Data Exploration", "About Us"])

with tab1:
    display_home()
with tab2:
    # Replace with your article recommendation function
    st.write("This will display article recommendations.")  # Placeholder for functionality
with tab3:
    display_data_exploration()
with tab4:
    display_about_us()


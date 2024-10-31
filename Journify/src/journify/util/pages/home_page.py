import streamlit as st
from PIL import Image

def home_page():
    #st.sidebar.image("intelligent_article_explorer_logo.png", use_column_width=True)
    
    # Sidebar navigation
    st.sidebar.title("Navigation")
    menu_options = ["Home", "Search Articles", "Q&A Chat Bot", "Submission Suggester", "Research Trendings", "About Us"]
    choice = st.sidebar.radio("Go to", menu_options)
    
    if choice == "Home":
        st.title("Welcome to Intelligent Article Explorer")
        st.write("Our platform utilizes advanced AI algorithms to offer you personalized article suggestions, quick summaries, and precise search results. Discover how each feature enhances your learning and keeps you updated on topics you care about.")
        
        # Start Exploring button
        if st.button("Start Exploring"):
            st.write("Redirecting to Search Articles...")
            # Redirect to Search Articles section
            show_search_section()
        
    elif choice == "Search Articles":
        show_search_section()
    
    elif choice == "Q&A Chat Bot":
        show_chatbot_section()
    
    elif choice == "Submission Suggester":
        show_suggester_section()
    
    elif choice == "Research Trendings":
        show_trendings_section()
    
    elif choice == "About Us":
        show_about_us()

# Sections Functions
def show_search_section():
    st.header("Smart Search")
    st.write("""
        Our search function leverages **Natural Language Processing (NLP)** and **Machine Learning** to deliver the most relevant articles based on your queries. 
        This search capability analyzes article content and metadata to understand context, synonyms, and popular topics.
        """)
    st.subheader("How it Works:")
    st.write("""
    - **Keyword Matching:** Matches keywords across titles, summaries, and tags for comprehensive results.
    - **Contextual Understanding:** Semantic analysis and NLP ensure that articles align with your exact needs.
    - **AI-Powered Ranking:** Articles are ranked by relevance, quality, and popularity, so the best content appears first.
    """)
    st.write("*Tips:* Use specific keywords or multiple keywords for more refined results.")

def show_chatbot_section():
    st.header("Q&A Chat Bot")
    st.write("""
        Our AI-driven Q&A bot provides instant responses to your questions based on article content, summaries, and other resources in our database.
        Gain insights, clarifications, and even article recommendations through intuitive and interactive conversation.
        """)
    st.subheader("How it Works:")
    st.write("""
    - **Contextual Querying:** The bot interprets the context of your questions and returns relevant answers from our knowledge base.
    - **Continuous Learning:** The bot evolves with new data, improving its accuracy and the relevance of its responses over time.
    """)
    st.write("*Tips:* Start with open-ended questions or specific queries for tailored responses.")

def show_suggester_section():
    st.header("Submission Suggester")
    st.write("""
        Based on your interests and past readings, we provide personalized article suggestions to keep you engaged with the latest content.
        This feature adapts and evolves with your reading patterns, ensuring a fresh, relevant feed every time.
        """)
    st.subheader("How it Works:")
    st.write("""
    - **Collaborative Filtering:** Our AI recommends articles by analyzing similar users' reading patterns.
    - **Content-Based Filtering:** Recommendations are tailored to your preferred topics and authors.
    - **Adaptive Algorithms:** Learns from your behavior to continually refine recommendations for an increasingly personalized experience.
    """)
    st.write("*Tips:* Engage with a variety of topics to see a broader range of recommendations.")

def show_trendings_section():
    st.header("Research Trendings")
    st.write("""
        Stay ahead with our trending articles feature, which showcases the latest and most popular research in real-time.
        Get insights into the most-discussed topics and explore trending publications in your areas of interest.
        """)
    st.subheader("How it Works:")
    st.write("""
    - **Real-Time Updates:** Trending topics are updated regularly to reflect the latest interests in various fields.
    - **Popular Metrics:** Content is prioritized based on readership and engagement metrics.
    """)
    st.write("*Tips:* Visit frequently to stay informed on current trends in your field.")

def show_about_us():
    st.header("About Us")
    st.write("""
        Intelligent Article Explorer is designed to enhance your research journey. Our team of developers, researchers, and data scientists created this tool 
        with the aim to facilitate efficient article discovery, summarization, and trend monitoring.
        """)
    st.write("For further information, contact us at: **contact@intelligentexplorer.com**")

# Main function to run the Streamlit application
if __name__ == "__main__":
    home_page()

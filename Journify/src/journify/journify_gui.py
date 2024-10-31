import warnings

warnings.simplefilter(action="ignore", category=FutureWarning)

import streamlit as st
from PIL import Image

from util.pages.home_page import home_page
#from util.pages.overview_page import overview_page
#from util.pages.articles_page import articles_page
#from util.pages.chatbot_page import chatbot_page
#from util.pages.supporter_page import supporter_page
#from util.pages.trendings_page import trendings_page
#from util.pages.about_page import about_page


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

        st.sidebar.markdown("## Main Menu")
        app = st.sidebar.selectbox(
            "Select Page", self.apps, format_func=lambda app: app["title"]
        )
        st.sidebar.markdown("---")
        app["function"]()


app = MultiApp()

app.add_app("Home Page", home_page)
#app.add_app("arXiv Overview", overview_page)
#app.add_app("Search Articles", articles_page)
#app.add_app("Q&A Chat Bot", chatbot_page)
#app.add_app("Submission Supporter", supporter_page)
#app.add_app("Research Trendings", trendings_page)
#app.add_app("About Us", about_page)

app.run()

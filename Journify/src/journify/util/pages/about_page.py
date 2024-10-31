import pandas as pd
import streamlit as st

# Set up the page layout
st.set_page_config(page_title="About Us - Intelligent Article Explorer", layout="wide")

# Header section
st.image("intelligent_article_explorer_logo.png", width=100)
st.title("About Intelligent Article Explorer")

# Navigation
st.markdown("""
<nav>
    <ul>
        <li><a href="welcome.html">Home</a></li>
        <li><a href="search.html">Search</a></li>
        <li><a href="summary.html">Summary</a></li>
        <li><a href="suggestion.html">Suggestion</a></li>
        <li><a href="trendings.html">Trendings</a></li>
        <li><a href="about.html">About Us</a></li>
    </ul>
</nav>
""", unsafe_allow_html=True)

# About Section
st.markdown("## About Intelligent Article Explorer")
#col1, col2 = st.columns(2)
#col1.image("intelligent_article_explorer_logo.png", caption="Intelligent Article Explorer Logo", width=150)
#col2.image("bach_khoa_university_logo.png", caption="Bach Khoa University Logo", width=150)

st.markdown("""
### Course Information
- **Course**: Intelligent Systems
- **Instructor**: Assoc. Prof. Quản Thành Thơ
- **Email**: [qttho@hcmut.edu.vn](mailto:qttho@hcmut.edu.vn)
""")

# Project Contributors
st.markdown("### Project Contributors")
contributors = {
    "Name": ["Huỳnh Thanh Tân", "Trần Quốc Thái", "Trần Vũ Hồng Thiên", "Rehman Ibtasam"],
    "Student ID": ["2392019", "2370759", "2370303", "2370300"],
    "Contact": [
        "httan.sdh241@hcmut.edu.vn",
        "tqthai.sdh232@hcmut.edu.vn",
        "tvhthien.sdh231@hcmut.edu.vn",
        "ribtasam.sdh231@hcmut.edu.vn"
    ]
}
df_contributors = pd.DataFrame(contributors)
st.table(df_contributors)

# Source Code and Support Links
st.markdown("### Source Code & Support")
st.markdown("""
- **Source Code**: [GitHub Repository](#)
- **Donate**: [Support Us](#)
""")

# Footer
st.markdown("---")
st.markdown("© 2024 Intelligent Article Explorer. All rights reserved.")

import streamlit as st
from streamlit.components.v1 import html
import pandas as pd

# Define a function to display the "About Us" section
def display_about_us():
    # Team member data
    team_members = [
        {
            "name": "Huỳnh Thanh Tân",
            "role": "Machine Learning Developer",
            "bio": "Tân has 1 year of experience in data science and specializes in NLP and recommendation systems.",
        },
        {
            "name": "Trần Quốc Thái",
            "role": "Data Developer",
            "bio": "Thái is a data wizard who ensures our systems run smoothly and efficiently with scalable infrastructure.",
        },
        {
            "name": "Trần Vũ Hồng Thiên",
            "role": "Machine Learning Developer",
            "bio": "With a deep passion for machine learning, Thiên focuses on developing robust models for recommendations.",
        },
        {
            "name": "Rehman Ibtasam",
            "role": "Data Developer",
            "bio": "Ibtasam designs intuitive and visually appealing data interfaces to make the Journify experience seamless.",
        }
    ]

    # CSS and HTML for team member cards and additional information
    html_content = """
    <style>
        /* Container styling */
        .container {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 30px;
            padding: 30px;
            width: 100%;
        }

        /* Row styling */
        .row {
            display: flex;
            flex-wrap: wrap;
            gap: 40px;
            justify-content: center;
            width: 100%;
        }

        /* Team member profile card styling */
        .profile-card {
            background: #f5f7f9;
            border-radius: 12px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.15);
            width: 280px;
            padding: 25px;
            text-align: center;
            transition: 0.3s;
        }
        .profile-card:hover {
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.25);
            transform: translateY(-6px);
        }
        .profile-card h3 {
            margin-top: 15px;
            color: #34495e;
            font-size: 1.6em;
        }
        .profile-card p {
            font-size: 1em;
            color: #7f8c8d;
            line-height: 1.5;
        }

        /* Course Information and Links section */
        .info-section {
            font-family: Arial, sans-serif;
            text-align: center;
            margin: 40px 0 20px;
            color: #2c3e50;
        }
        .info-section h3 {
            font-size: 1.8em;
            color: #2980b9;
        }
        .info-section p, .info-section a {
            font-size: 1em;
            color: #2c3e50;
        }
        .info-section a:hover {
            color: #2980b9;
            text-decoration: underline;
        }
    </style>
    
    <div class="info-section">
        <h3>About Intelligent Article Explorer</h3>
        <p>Welcome to the Intelligent Article Explorer, developed as part of the Intelligent Systems course.</p>
        <p><strong>Course:</strong> Intelligent Systems</p>
        <p><strong>Instructor:</strong> Assoc. Prof. Quản Thành Thơ</p>
        <p><strong>Email:</strong> <a href="mailto:qttho@hcmut.edu.vn">qttho@hcmut.edu.vn</a></p>
    </div>

    <!-- Team Member Cards -->
    <div class='container'>
        <div class='row'>
    """

    # Generate HTML for each team member card
    for member in team_members:
        html_content += f"""
            <div class='profile-card'>
                <h3>{member["name"]}</h3>
                <p><strong>{member["role"]}</strong></p>
                <p>{member["bio"]}</p>
            </div>
        """
    html_content += """
        </div> <!-- Close row div -->
    </div> <!-- Close container div -->

    <!-- Additional Links Section -->
    <div class="info-section">
        <h3>Source Code & Support</h3>
        <p><a href="#">GitHub Repository</a></p>
        <p><a href="#">Support Us</a></p>
    </div>
    """

    html(html_content, height=1000)

# Display the page content
st.title("About Us")
display_about_us()

# Data table for additional contributor information
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

# Footer
st.markdown("---")
st.markdown("© 2024 Intelligent Article Explorer. All rights reserved.")

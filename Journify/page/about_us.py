import streamlit as st
from streamlit.components.v1 import html

# Define a function to display the "About Us" section
def display_about_us():
    # Team member data with refined project contributions and linked emails
    team_members = [
        {
            "name": "Huỳnh Thanh Tân",
            "role": "Machine Learning Developer",
            "id": "2392019",
            "email": "mailto:httan.sdh241@hcmut.edu.vn",
            "contribution": "Developed advanced NLP algorithms to enhance recommendation precision for the Intelligent Article Explorer."
        },
        {
            "name": "Trần Quốc Thái",
            "role": "Data Developer",
            "id": "2370759",
            "email": "mailto:tqthai.sdh232@hcmut.edu.vn",
            "contribution": "Engineered scalable data infrastructure, ensuring reliable performance and seamless data processing."
        },
        {
            "name": "Trần Vũ Hồng Thiên",
            "role": "Machine Learning Developer",
            "id": "2370303",
            "email": "mailto:tvhthien.sdh231@hcmut.edu.vn",
            "contribution": "Designed and optimized ML models, improving the efficiency and accuracy of recommendation features."
        },
        {
            "name": "Rehman Ibtasam",
            "role": "Data Developer",
            "id": "2370300",
            "email": "mailto:ribtasam.sdh231@hcmut.edu.vn",
            "contribution": "Developed user-friendly interfaces, providing a seamless experience for data visualization and exploration."
        }
    ]

    # CSS and HTML for team member cards and additional information
    html_content = """
    <style>
        .container {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 20px;
            padding: 20px;
        }
        .row {
            display: flex;
            gap: 30px;
            justify-content: center;
            width: 100%;
            flex-wrap: wrap;
        }
        .profile-card {
            background: #f9f9f9;
            border-radius: 15px;
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
            overflow: hidden;
            transition: 0.3s ease;
            width: 280px;
            padding: 20px;
            text-align: center;
            font-family: Arial, sans-serif;
        }
        .profile-card:hover {
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
            transform: translateY(-5px);
        }
        .profile-card h3 {
            margin: 10px 0;
            font-size: 1.5em;
            color: #333;
        }
        .profile-card p {
            color: #555;
            font-size: 1em;
            margin: 5px 0;
            line-height: 1.5em;
        }
        .profile-card .contact-info {
            margin-top: 10px;
            font-size: 0.9em;
        }
        .contact-info a {
            color: #3498db;
            text-decoration: none;
        }
        .contact-info a:hover {
            text-decoration: underline;
        }
        .info-section {
            text-align: center;
            font-family: Arial, sans-serif;
            margin-top: 20px;
        }
        .info-section h3 {
            font-size: 1.8em;
            margin-bottom: 5px;
        }
        .info-section p {
            font-size: 1em;
            color: #555;
        }
    </style>
    
    <div class="info-section">
        <h3>Intelligent Article Explorer</h3>
        <p><strong>Course:</strong> Intelligent Systems</p>
        <p><strong>Instructor:</strong> Assoc. Prof. Quản Thành Thơ</p>
        <p><strong>Email:</strong> <a href="mailto:qttho@hcmut.edu.vn">qttho@hcmut.edu.vn</a></p>
        <h3>Project Contributors</h3>
    </div>
    
    <!-- Team Member Cards -->
    <div class='container'>
    """

    # Generate HTML for each team member in two-member rows
    for i in range(0, len(team_members), 2):
        html_content += "<div class='row'>"
        for member in team_members[i:i+2]:  # Two members per row
            html_content += f"""
            <div class='profile-card'>
                <h3>{member["name"]}</h3>
                <p><strong>{member["role"]}</strong></p>
                <p>{member["contribution"]}</p>
                <div class="contact-info">
                    <p><strong>ID:</strong> {member["id"]}</p>
                    <p><strong>Email:</strong> <a href="{member["email"]}">{member["email"].replace("mailto:", "")}</a></p>
                </div>
            </div>
            """
        html_content += "</div>"  # Close the row div
    html_content += "</div>"  # Close the container div

    html(html_content, height=1200)

# Display the about us page
display_about_us()

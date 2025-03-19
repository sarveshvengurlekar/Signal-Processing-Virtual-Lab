import streamlit as st  # Import Streamlit for web app creation
import base64  # Import base64 for encoding images
import os  # Import os to check file paths

# Set Streamlit page configuration
st.set_page_config(
    page_title="Signal Processing Virtual Lab",
    layout="wide",
    page_icon=" "  # Placeholder for page icon
)

# Function to encode an image as a Base64 string
def get_base64_image(image_path):
    """Encodes an image file to Base64 format."""
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except Exception as e:
        st.error(f"Error encoding image: {e}")
        return None

# Paths to logo and banner images
logo_path = "static/fcritlogo.png"  # Ensure this path is correct
banner_path = "Media/Website_Banner.jpeg"  # Ensure this path is correct

# Encode images in Base64
logo_base64 = get_base64_image(logo_path)
banner_base64 = get_base64_image(banner_path)

# Inject custom CSS for header styling
st.markdown(
    f"""
    <style>
    .header {{
        position: fixed;
        left: 0;
        top: 0;
        width: 100%;
        height: 148px;
        background-color: #00b3ff;
        color: #FFFFFF;
        text-align: center;
        padding: 90px 10px;
        z-index: 1000;
        overflow: hidden;
        display: flex;
        align-items: center;
        justify-content: space-between;
    }}

    .header-content {{
        flex-grow: 1;
        text-align: center;
    }}
    

    .header p {{
        font-family: "Times New Roman", Times, serif;
        font-size: 15px;
        line-height: 1.2;
        margin: 5px 0;
    }}

    .header p1 {{
        font-family: "Times New Roman", Times, serif;
        font-size: 30px;
        line-height: 1.2;
        margin: 5px 0;
    }}

    .header-content {{
        flex-grow: 1;
        text-align: center;
        padding-top: 50px; /* Adjust this value to move text down */
    }}

    .logo-container {{
        padding-right: 20px;
        padding-top: 60px;
    }}

    .logo-container img {{
        width: 100px;
        height: auto;
    }}
    .stApp {{
        margin-top: 180px; /* Push content below the fixed header */
        padding-bottom: 80px; /* Avoid footer overlap */
    }}

    .footer {{
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        height: 42px;
        background-color: #00b3ff;
        color: #FFFFFF;
        text-align: center;
        padding: 10px;
        font-size: 14px;
        z-index: 1000;
    }}
    </style>

    <!-- Header section with logo on the top-right corner -->
    <div class="header">
        <div class="header-content">
            <p><b>AGNEL CHARITIES</b></p>
            <p1><b>FR. C. RODRIGUES INSTITUTE OF TECHNOLOGY</b></p1>
            <p>Agnel Technical Education Complex Sector 9-A, Vashi, Navi Mumbai, Maharashtra, India PIN - 400703</p>
            <p>(An Autonomous Institute & Permanently Affiliated To University Of Mumbai)</p>
        </div>
        <div class="logo-container">
            <img src="data:image/png;base64,{logo_base64}" alt="Institute Logo">
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# Inject custom CSS for footer
st.markdown(
    """
    <div class="footer">
        <p>© 2025 Fr. Conceicao Rodrigues Institute of Technology. All rights reserved.</p>
    </div>
    """, 
    unsafe_allow_html=True
)

# Hide Streamlit default menu
hide_menu = """
<style>
#MainMenu {
visibility:hidden;
}
</style>
"""

# Remove unnecessary UI elements
st.markdown("""<style>[data-testid="stDecoration"] { display: none; }</style>""", unsafe_allow_html=True)
st.markdown(hide_menu, unsafe_allow_html=True)  # Apply hidden menu style


st.markdown("<h1 style='text-align: center; color: black;'> Our Vision </h1>", unsafe_allow_html=True)
st.markdown(
    "<p style='font-size:28px; text-align: justify;'>"
    "The <b>Signal Processing Virtual Lab</b> is an advanced digital learning platform developed by the <b>Electronics & Telecommunication Department of Fr. C. Rodrigues Institute of Technology.</b>""</p>" 
    "<p" "It is designed to bridge the gap between theoretical concepts and practical applications in signal processing by offering an interactive and immersive learning experience.""</p"
    "By leveraging state-of-the-art computational tools, the platform allows users to analyze, observe, and interpret various signal characteristics through real-time graphical representations." 
    "This hands-on approach enhances conceptual understanding and fosters deeper insights into fundamental and advanced signal processing techniques." 
    "Users can engage with a wide range of signal transformations, filtering methods, spectral analysis, and system responses, providing a comprehensive learning experience."
    "The platform is particularly beneficial for academic institutions, enabling seamless integration into coursework, laboratory exercises, and research projects." 
    "Additionally, it supports self-paced learning, allowing users to experiment with different signal processing operations," 
    "visualize real-time changes, and develop a practical understanding of abstract mathematical concepts."
    "</p>",
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)

# Key Features with Increased Text Size
st.markdown("<h1 style='color: black;'> • Key Features</h1>", unsafe_allow_html=True)

features = [
    "<b>Interactive Learning:</b> Explore and visualize fundamental signal processing concepts through simulations.",
    "<b>Dynamic Visualizations:</b> Gain insights into signal behavior with real-time graphical representations.",
    "<b>Unrestricted Accessibility:</b> Access the lab anytime, anywhere, without the need for physical equipment.",
    "<b>Conceptual Clarity:</b> Strengthen understanding of signal properties, transformations, and system behavior.",
    "<b>Bridging Theory and Visualization:</b> Enhance learning by observing how theoretical concepts translate into signal representations."
]

# Display Key Features with Larger Font
for feature in features:
    st.markdown(f"<p style='font-size:28px;'> - {feature}</p>", unsafe_allow_html=True)


st.header("")

st.header("</> Developers Team", divider="blue")

st.header("")

linkedin_pranali = "https://www.linkedin.com/in/pranali-choudhari-89aa4215/"
email_pranali = "mailto:pranali.choudhari@fcrit.ac.in"
linkedin_sarvesh = "https://www.linkedin.com/in/sarvesh-vengurlekar-"
email_sarvesh = "mailto:sarveshvengurlekarwork@gmail.com"
linkedin_keziah = "https://www.linkedin.com/in/keziah-vinod-948a32340"
email_keziah = "mailto:keziahvinod2004@gmail.com"
linkedin_riya = "https://www.linkedin.com/in/riya-parab-455118241/"
email_riya = "mailto:riyaramchandraparab@gmail.com"
linkedin_aaditi = "https://www.linkedin.com/in/aaditi-narvekar-5128a2341/"
email_aaditi = "mailto:aaditinarvekar1001@gmail.com"


# UI Design
col1, col2, col3 = st.columns(3)

with col2:
    with st.container():
        st.markdown(
            f"""
        <style>
            .profile-card {{
                text-align: center;
                background: #0069FF;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
                display: inline-block;
            }}
            .name {{
                font-size: 24px;
                font-weight: bold;
                margin-top: 10px;
                color: white;
            }}
            .title {{
                font-size: 16px;
                color: white;
                margin-top: 5px;
            }}
            .button-container {{
                display: flex;
                flex-direction: column;
                align-items: center;
                margin-top: 10px;
            }}
            .button {{
                background-color: white;
                border: none;
                padding: 10px 15px;
                text-align: center;
                font-size: 16px;
                border-radius: 5px;
                cursor: pointer;
                text-decoration: none;
                margin: 5px;
                display: inline-flex;
                align-items: center;
                gap: 10px;
            }}
            .linkedin-button {{
                color: black;
            }}
            .icon {{
                width: 20px;
                height: 20px;
            }}
        </style>
        <div class="profile-card">
            <div class="name">Dr. Pranali Choudhari</div>
            <div class="title">Mentor</div>
                <a href="{linkedin_pranali}" target="_blank" class="button linkedin-button">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png" class="icon">
                </a>
                <a href="{email_pranali}" class="button">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/4/4e/Gmail_Icon.png" class="icon">
                </a>
            </div>
        </div>
              """,
        unsafe_allow_html=True)

st.header(" ")

col1, col2, col3, col4 = st.columns(4)

with col1:
    with st.container():
        st.markdown(
            f"""
        <style>
            .profile-card {{
                text-align: center;
                background: #00b3ff;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
                display: inline-block;
            }}
            .name {{
                font-size: 24px;
                font-weight: bold;
                margin-top: 10px;
                color: white;
            }}
            .title {{
                font-size: 16px;
                color: white;
                margin-top: 5px;
            }}
            .button-container {{
                display: flex;
                flex-direction: column;
                align-items: center;
                margin-top: 10px;
            }}
            .button {{
                background-color: white;
                border: none;
                padding: 10px 15px;
                text-align: center;
                font-size: 16px;
                border-radius: 5px;
                cursor: pointer;
                text-decoration: none;
                margin: 5px;
                display: inline-flex;
                align-items: center;
                gap: 10px;
            }}
            .linkedin-button {{
                color: black;
            }}
            .icon {{
                width: 20px;
                height: 20px;
            }}
        </style>
        <div class="profile-card">
            <div class="name">Sarvesh Udaykumar Vengurlekar</div>
            <div class="title">Developer</div>
                <a href="{linkedin_sarvesh}" target="_blank" class="button linkedin-button">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png" class="icon">
                </a>
                <a href="{email_sarvesh}" class="button">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/4/4e/Gmail_Icon.png" class="icon">
                </a>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
        
    st.header(" ")
    
with col3:        
    with st.container():
        st.markdown(
            f"""
        <style>
            .profile-card {{
                text-align: center;
                background: #00b3ff;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
                display: inline-block;
            }}
            .name {{
                font-size: 24px;
                font-weight: bold;
                margin-top: 10px;
                color: white;
            }}
            .title {{
                font-size: 16px;
                color: white;
                margin-top: 5px;
            }}
            .button-container {{
                display: flex;
                flex-direction: column;
                align-items: center;
                margin-top: 10px;
            }}
            .button {{
                background-color: white;
                border: none;
                padding: 10px 15px;
                text-align: center;
                font-size: 16px;
                border-radius: 5px;
                cursor: pointer;
                text-decoration: none;
                margin: 5px;
                display: inline-flex;
                align-items: center;
                gap: 10px;
            }}
            .linkedin-button {{
                color: black;
            }}
            .icon {{
                width: 20px;
                height: 20px;
            }}
        </style>
        <div class="profile-card">
            <div class="name">Keziah Mariam Vinod</div>
            <div class="title">Developer</div>
                <a href="{linkedin_keziah}" target="_blank" class="button linkedin-button">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png" class="icon">
                </a>
                <a href="{email_keziah}" class="button">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/4/4e/Gmail_Icon.png" class="icon">
                </a>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


with col2:
    with st.container():
        st.markdown(
            f"""
        <style>
            .profile-card {{
                text-align: center;
                background: #0069FF;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
                display: inline-block;
            }}
            .name {{
                font-size: 24px;
                font-weight: bold;
                margin-top: 10px;
                color: white;
            }}
            .title {{
                font-size: 16px;
                color: white;
                margin-top: 5px;
            }}
            .button-container {{
                display: flex;
                flex-direction: column;
                align-items: center;
                margin-top: 10px;
            }}
            .button {{
                background-color: white;
                border: none;
                padding: 10px 15px;
                text-align: center;
                font-size: 16px;
                border-radius: 5px;
                cursor: pointer;
                text-decoration: none;
                margin: 5px;
                display: inline-flex;
                align-items: center;
                gap: 10px;
            }}
            .linkedin-button {{
                color: black;
            }}
            .icon {{
                width: 20px;
                height: 20px;
            }}
        </style>
        <div class="profile-card">
            <div class="name">Riya Ramchandra Parab</div>
            <div class="title">Developer</div>
                <a href="{linkedin_riya}" target="_blank" class="button linkedin-button">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png" class="icon">
                </a>
                <a href="{email_riya}" class="button">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/4/4e/Gmail_Icon.png" class="icon">
                </a>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
        
    st.header(" ")
    
with col4:        
    with st.container():
        st.markdown(
            f"""
        <style>
            .profile-card {{
                text-align: center;
                background: #00b3ff;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
                display: inline-block;
            }}
            .name {{
                font-size: 24px;
                font-weight: bold;
                margin-top: 10px;
                color: white;
            }}
            .title {{
                font-size: 16px;
                color: white;
                margin-top: 5px;
            }}
            .button-container {{
                display: flex;
                flex-direction: column;
                align-items: center;
                margin-top: 10px;
            }}
            .button {{
                background-color: white;
                border: none;
                padding: 10px 15px;
                text-align: center;
                font-size: 16px;
                border-radius: 5px;
                cursor: pointer;
                text-decoration: none;
                margin: 5px;
                display: inline-flex;
                align-items: center;
                gap: 10px;
            }}
            .linkedin-button {{
                color: black;
            }}
            .icon {{
                width: 20px;
                height: 20px;
            }}
        </style>
        <div class="profile-card">
            <div class="name">Aaditi Manojkumar Narvekar</div>
            <div class="title">Developer</div>
                <a href="{linkedin_aaditi}" target="_blank" class="button linkedin-button">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png" class="icon">
                </a>
                <a href="{email_aaditi}" class="button">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/4/4e/Gmail_Icon.png" class="icon">
                </a>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
st.markdown('</div>', unsafe_allow_html=True)

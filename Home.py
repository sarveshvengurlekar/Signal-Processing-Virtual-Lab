import streamlit as st  # Import Streamlit for web app creation
import base64  # Import base64 for encoding images
import os  # Import os to check file paths

# Set Streamlit page configuration
st.set_page_config(
    page_title="Signals & Systems Virtual Lab",
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
logo_path = r"static/fcritlogo.png"
banner_path = r"Media/Website_Banner.jpeg"

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
        background-color: #0069FF;
        color: #FFFFFF;
        text-align: left;
        padding: 20px 30px;
        z-index: 1000;
        overflow: hidden;
        display: flex;
        align-items: center;
        justify-content: space-between;
    }}

    .header h1 {{
        margin-top: 48px;
        font-size: 30px;
        line-height: 2.5;
    }}

    .logo-container {{
        position: absolute;
        top: 62px;
        right: 20px;
    }}

    .stApp {{
        margin-top: 146px; /* Push content below the fixed header */
        padding-bottom: 80px; /* Avoid footer overlap */
    }}

    .footer {{
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        height: 42px;
        background-color: #0069FF;
        color: #FFFFFF;
        text-align: center;
        padding: 10px;
        font-size: 14px;
        z-index: 1000;
    }}
    </style>
    
    <!-- Header section with logo -->
    <div class="header">
        <h1>Fr. Conceicao Rodrigues Institute of Technology</h1>
        <div class="logo-container">
            <img src="data:image/png;base64,{logo_base64}" width="75">
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

# Display page title with a divider
st.header("Welcome to Signals Processing Virtual Lab", divider=True)

# Centered banner image using Base64 encoding
if banner_base64:
    st.markdown(
        f"""
        <style>
        .banner-container {{
            text-align: center;
            margin-top: 20px;
        }}
        .banner-container img {{
            width: 80%;
            max-width: 900px;
            border-radius: 10px;
        }}
        </style>
        <div class="banner-container">
            <img src="data:image/jpeg;base64,{banner_base64}" alt="Website Banner">
        </div>
        """,
        unsafe_allow_html=True
    )
else:
    st.error("Failed to load the banner image. Please check the file path.")

# Empty header with blue divider (used for spacing)
st.header("</> Developers Team", divider="blue")

st.header("")

linkedin_pranali = "https://www.linkedin.com/in/pranali-choudhari-89aa4215/"
email_pranali = "mailto:pranali.choudhari@fcrit.ac.in"
linkedin_sarvesh = "https://www.linkedin.com/in/sarvesh-vengurlekar-"
email_sarvesh = "mailto:3022170@extc.fcrit.ac.in"
linkedin_keziah = "https://www.linkedin.com/in/keziah-vinod-948a32340"
email_keziah = "mailto:3022125@extc.fcrit.ac.in"
linkedin_riya = "https://www.linkedin.com/in/riya-parab-455118241/"
email_riya = "mailto:3022168@extc.fcrit.ac.in"
linkedin_aaditi = "https://www.linkedin.com/in/aaditi-narvekar-5128a2341/"
email_aaditi = "mailto:3022136@extc.fcrit.ac.in"


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
        unsafe_allow_html=True
    )

st.header(" ")

col1, col2, col3 = st.columns(3)

with col1:
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


with col3:
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

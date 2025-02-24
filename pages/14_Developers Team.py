import streamlit as st 
import base64

st.set_page_config(
    page_title="Signals & Systems Virtual Lab",
    layout="wide",
    page_icon=" "
)

# Function to encode image in Base64
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Path to logo
logo_path = r"C:\Users\sarve\Downloads\Coding\Python\DSP Internship\Streamlit\Signals & System Virtual Lab\static\fcritlogo.png"
logo_base64 = get_base64_image(logo_path)

# Header with embedded Base64 logo
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
        margin-top: 146px; /* Ensure content starts below the fixed header */
        padding-bottom: 80px; /* Prevent overlap with the footer */
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
    
    <div class="header">
        <h1>Fr. Conceicao Rodrigues Institute of Technology</h1>
        <div class="logo-container">
            <img src="data:image/png;base64,{logo_base64}" width="75">
        </div>
    </div>
    """, 
    unsafe_allow_html=True
)

# Footer
st.markdown(
    """
    <div class="footer">
        <p>© 2025 Fr. Conceicao Rodrigues Institute of Technology. All rights reserved.</p>
    </div>
    """, 
    unsafe_allow_html=True
)

hide_menu= """
<style>
#MainMenu {
visibility:hidden;
}
</style>
"""

st.markdown("""
<style>
	[data-testid="stDecoration"] {
		display: none;
	}

</style>""",
unsafe_allow_html=True)

st.markdown(hide_menu, unsafe_allow_html=True)

st.header("</>  Developers Team", divider=True)

st.markdown("""

The **Signal & System Virtual Lab Web Portal** is developed by  **Fr. Conceicao Rodrigues Institute of Technology (FCRIT)**, Students of the **Electronics & Telecommunication (EXTC) Department**  under the mentorship of **Dr. Pranali Choudhari**.  
This platform enhances the **learning experience for students** and provides **better teaching methods for faculty**.  

""")

with st.container():
    st.markdown(
        """
        <div style="text-align: center;">
            <h2>Mentor :-</h2>
            <h2>Name : Dr. Pranali Choudhari</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

    linkedin_pranali = "https://www.linkedin.com/in/pranali-choudhari-89aa4215/"
    email_pranali = "mailto:pranali.choudhari@fcrit.ac.in"

    st.markdown(
        f"""
        <div style="display: flex; flex-direction: column; align-items: center; margin-top: 10px;">
            <a href="{linkedin_pranali}" target="_blank">
                <button style="background-color:#0077b5; color:white; border:none; padding:10px 15px; 
                text-align:center; font-size:16px; border-radius:5px; cursor:pointer;">
                    Connect on LinkedIn
                </button>
            </a>
            <br>
            <a href="{email_pranali}">
                <button style="background-color:#0077b5; color:white; border:none; padding:10px 25px; 
                text-align:center; font-size:16px; border-radius:5px; cursor:pointer;">
                    Connect via Email
                </button>
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )


st.header(" ")

# Display Name and Email
# Create two columns
col1, col2, col3 = st.columns(3)

# Left Column - Sarvesh Udaykumar Vengurlekar
with col1:
    st.markdown("## Developer 1 :-")
    st.markdown("## Name : Sarvesh Udaykumar Vengurlekar")

    linkedin_sarvesh = "https://www.linkedin.com/in/sarvesh-vengurlekar-"
    email_sarvesh = "mailto:3022170@extc.fcrit.ac.in"

    st.markdown(f"""
        <div style="display: flex; align-items: center; gap: 15px; margin-top: 10px;">
            <a href="{linkedin_sarvesh}" target="_blank">
                <button style="background-color:#0077b5; color:white; border:none; padding:10px 15px; 
                text-align:center; font-size:16px; border-radius:5px; cursor:pointer;">
                    Connect on LinkedIn
                </button>
            </a>
        </div>

         <div style="display: flex; align-items: center; gap: 15px; margin-top: 10px;">   
            <a href="{email_sarvesh}">
                <button style="background-color:#0077b5; color:white; border:none; padding:10px 25px; 
                text-align:center; font-size:16px; border-radius:5px; cursor:pointer;">
                    Connect via Email
                </button>
            </a>
        </div>
    """, unsafe_allow_html=True)

    st.header(" ")

    st.markdown("## Developer 3 :-")
    st.markdown("## Name : Keziah Mariam Vinod")

    linkedin_keziah = "https://www.linkedin.com/in/keziah-vinod-948a32340"
    email_keziah = "mailto:3022125@extc.fcrit.ac.in"

    st.markdown(f"""
        <div style="display: flex; align-items: center; gap: 15px; margin-top: 10px;">
            <a href="{linkedin_keziah}" target="_blank">
                <button style="background-color:#0077b5; color:white; border:none; padding:10px 15px; 
                text-align:center; font-size:16px; border-radius:5px; cursor:pointer;">
                    Connect on LinkedIn
                </button>
            </a>
        </div>

         <div style="display: flex; align-items: center; gap: 15px; margin-top: 10px;">   
            <a href="{email_keziah}">
                <button style="background-color:#0077b5; color:white; border:none; padding:10px 25px; 
                text-align:center; font-size:16px; border-radius:5px; cursor:pointer;">
                    Connect via Email
                </button>
            </a>
        </div>
    """, unsafe_allow_html=True)


with col3:
    st.markdown("## Developer 2 :-")
    st.markdown("## Name : Riya Ramchandra Parab")

    linkedin_riya = "https://www.linkedin.com/in/riya-parab-455118241/"
    email_riya = "mailto:3022168@extc.fcrit.ac.in"

    st.markdown(f"""
        <div style="display: flex; align-items: center; gap: 15px; margin-top: 10px;">
            <a href="{linkedin_riya}" target="_blank">
                <button style="background-color:#0077b5; color:white; border:none; padding:10px 15px; 
                text-align:center; font-size:16px; border-radius:5px; cursor:pointer;">
                    Connect on LinkedIn
                </button>
            </a>
        </div>

         <div style="display: flex; align-items: center; gap: 15px; margin-top: 10px;">   
            <a href="{email_riya}">
                <button style="background-color:#0077b5; color:white; border:none; padding:10px 25px; 
                text-align:center; font-size:16px; border-radius:5px; cursor:pointer;">
                    Connect via Email
                </button>
            </a>
        </div>
    """, unsafe_allow_html=True)

    st.header(" ")

    st.markdown("## Developer 4 :-")
    st.markdown("## Name : Aaditi Manojkumar Narvekar")

    linkedin_aaditi = "https://www.linkedin.com/in/aaditi-narvekar-5128a2341/"
    email_aaditi = "mailto:3022136@extc.fcrit.ac.in"

    st.markdown(f"""
        <div style="display: flex; align-items: center; gap: 15px; margin-top: 10px;">
            <a href="{linkedin_aaditi}" target="_blank">
                <button style="background-color:#0077b5; color:white; border:none; padding:10px 15px; 
                text-align:center; font-size:16px; border-radius:5px; cursor:pointer;">
                    Connect on LinkedIn
                </button>
            </a>
        </div>

         <div style="display: flex; align-items: center; gap: 15px; margin-top: 10px;">   
            <a href="{email_aaditi}">
                <button style="background-color:#0077b5; color:white; border:none; padding:10px 25px; 
                text-align:center; font-size:16px; border-radius:5px; cursor:pointer;">
                    Connect via Email
                </button>
            </a>
        </div>
    """, unsafe_allow_html=True)



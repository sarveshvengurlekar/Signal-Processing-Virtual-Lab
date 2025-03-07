import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import wave
import base64
from scipy.signal import resample

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
        margin-top: 100px; /* Push content below the fixed header */
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

st.header("Nyquist Sampling Theorem", divider=True)

st.markdown("""
The **Nyquist Sampling Theorem** is a fundamental principle in **signal processing** that defines the minimum sampling rate required to accurately reconstruct a continuous-time signal from its samples.  
This theorem plays a crucial role in **digital audio, communications, and data acquisition systems**.
""")

# Nyquist Theorem Definition
st.subheader("- Nyquist Sampling Theorem")
st.markdown("The theorem states that a band-limited signal with a maximum frequency component of must be sampled at a rate of at least **twice its highest frequency** to ensure perfect reconstruction:")

st.latex(r"f_s \geq 2 f_{max}")

st.markdown("""
The Failure to satisfy this condition results in **aliasing**, where high-frequency components appear as low-frequency distortions.
""")

# Graphical & Audible Analysis
st.subheader("- Real-Time Analysis")
st.markdown("""
- **Graphical Visualization:** Observe the effects of **under-sampling, proper sampling, and over-sampling** in real-time.  
- **Audible Feedback:** Hear the reconstructed audio at different sampling rates to understand the impact on sound quality.  
""")

# Applications
st.subheader("- Applications")
st.markdown("""
- **Digital Audio Processing**: Ensures high-fidelity sound reproduction.  
- **Telecommunications**: Prevents signal distortion in data transmission.  
- **Medical Imaging**: Used in MRI and CT scan reconstruction.  
- **Radar & Sonar**: Optimizes signal detection and tracking.
""")

# Conclusion
st.markdown("""
This tool is valuable for **engineers, researchers, and students** in **signal processing, telecommunications, and real-time system design**.
""")

st.header("",divider="blue")

video_options = {
    "Nyquist Sampling Theorem" : r"Media/Nyquist (2).mp4",
}

# Dropdown to select video
selected_video = st.selectbox("Select Nyquist Video", list(video_options.keys()), index=0)

# Display selected video
st.video(video_options[selected_video])

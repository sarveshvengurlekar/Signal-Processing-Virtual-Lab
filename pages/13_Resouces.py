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

# Streamlit app title
st.header("Resources", divider=True)


col1, col2, col3 = st.columns(3)

# File path
LTI_file_path = r"C:\Users\sarve\Downloads\Coding\Python\DSP Internship\Streamlit\Signals & System Virtual Lab\Resources\LTI_Sample_Audio.wav"
Sampling_file_path =r"C:\Users\sarve\Downloads\Coding\Python\DSP Internship\Streamlit\Signals & System Virtual Lab\Resources\Sampling_Thm_Audio.wav"
ECG_file_path = r"C:\Users\sarve\Downloads\Coding\Python\DSP Internship\Streamlit\Signals & System Virtual Lab\Resources\ECG_sample_sig.mat"

# Read the file in binary mode
with open(LTI_file_path, "rb") as file:
    file_data = file.read()

with open(Sampling_file_path, "rb") as file:
    file_data = file.read()

with open(ECG_file_path, "rb") as file:
    file_data = file.read()

with col1:
    st.write("## - LTI Sample Audio")
    # Display download button
    st.download_button(
        key=1,
        label="Download Audio",
        data=file_data,
        file_name="LTI_Sample_Audio.wav",
        mime="audio/wav"
    )

with col2:
    st.write("## - Nyquist Sampling Theorem")
    # Display download button
    st.download_button(
        key=2,
        label="Download Audio",
        data=file_data,
        file_name="Sampling_Sample_Audio.wav",
        mime="audio/wav"
    )

with col3:
    st.write("## - QRS Filteration")
    # Display download button
    st.download_button(
        key=3,
        label="Download Data",
        data=file_data,
        file_name="ECG_sample_sig.mat",
        mime="application/octet-stream"
    )
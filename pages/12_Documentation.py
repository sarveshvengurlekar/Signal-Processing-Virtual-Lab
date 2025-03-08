import streamlit as st
import base64

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


# Streamlit app title
st.header("Documentation", divider=True)

st.write("## - Operations on Signals")
st.write("""
1. Click on the Operations on Signals section.
2. Enter values for eight parameters:
   - **Amplitude 1 & 2**
   - **Frequency 1 & 2**
   - **Phase Shift 1 & 2**
   - **Function 1 & 2** (dropdown: sin, cos, square)
   - **Time duration**
   - **Operation type** (dropdown: addition, multiplication, subtraction)
3. Click the “Plot” button to visualize six waveforms:
   - **1st waveform:** Signal 1
   - **2nd waveform:** Frequency spectrum of Signal 1
   - **3rd waveform:** Signal 2
   - **4th waveform:** Frequency spectrum of Signal 2
   - **5th waveform:** Resultant signal
   - **6th waveform:** Frequency spectrum of result signal
""")

st.write("## - Even and Odd Signals")
st.write("""
1. Click on the Even and Odd Signals section.
2. Select a signal (e.g., sine, cosine, exponent).
3. Click the plot button to generate three waveforms:
   - **1st waveform:** Original signal.
   - **2nd waveform:** Even component.
   - **3rd waveform:** Odd component.
""")

st.write("## - Nyquist Sampling Theorem")
st.write("""
1. **Click on Signal Source** to select the source from:
   - Generate Tone  
   - Upload Audio File (.wav)

2. If you selected **Generate Tone**, then Tone Generation parameters will appear, where a **sine wave** is generated.

3. You can set the **Maximum Frequency**, **Sampling Rate**, and **Duration** of the generated tone.

4. If you selected **Upload Audio File (.wav)**:
   - Upload a **.wav** audio file from your desktop.  
   - If you don’t have a **.wav** file, use the provided audio in the **Nyquist Sampling Theorem** section.

5. After selecting the **Signal Source**, scroll down to enter the sampling frequency for:
   - **Undersampling** (Fs < Fm)  
   - **Critical Sampling** (Fs = Fm)  
   - **Oversampling** (Fs > 2Fm)  

6. After entering the frequency values, **play the audio** and analyze the **Time Domain** and **Frequency Domain** plots of the signal.
""")


st.write("## - Autocorrelation")
st.write("""
1. Click on the Autocorrelation section
.
2. Click the dropdown and select or enter signals (e.g., sin, cos, square).
3. Click the plot button to generate the waveform.
4. The waveform will display four subplots:
   - **1st subplot:** Original signal (e.g., "Original sine signal").
   - **2nd subplot:** Noisy signal.
   - **3rd subplot:** Autocorrelation results.
   - **4th subplot:** ESD signal.
""")

st.write("## - Cross-Correlation")
st.write("""
1. Click on the Cross-Correlation section.
2. Click the dropdown and select or enter signals.
3. Click the plot button to generate the waveform.
4. The waveform contains four subplots (same as Autocorrelation), except ESD is not included in Cross-Correlation.
""")


st.write("## - Discrete Fourier Transform (DFT)")
st.write("""
1. Click on Discrete Fourier Transform (DFT) section.
2. Select one of the four options:
   - 4-point DFT (DIT Type)
   - 4-point DFT (DIF Type)
   - 8-point DFT (DIT Type)
   - 8-point DFT (DIF Type)
3. Click the play button to visualize the animation.
4. The animation can be paused by clicking the play button again.
""")


st.write("## - QRS Complex Filtration")
st.write("""
1. Click on the QRS Complex Filtration section.
3. Click the “Browse files” button to upload a **.mat file**, if you don't have .mat file then go to Resources section & download the file for QRS Complex Filtration.
4. Upon successful upload, a message **“.mat file loaded successfully!”** will be displayed.
5. Below this message, a correlation analysis will be visualized in three waveforms:
   - **1st waveform:** Original ECG cycle.
   - **2nd waveform:** Noisy ECG cycle.
   - **3rd waveform:** Filtered ECG cycle.
""")

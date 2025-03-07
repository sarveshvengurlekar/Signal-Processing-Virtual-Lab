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
logo_path = r"static/fcritlogo.png"
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
        background-color: #00b3ff;
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
        background-color: #00b3ff;
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

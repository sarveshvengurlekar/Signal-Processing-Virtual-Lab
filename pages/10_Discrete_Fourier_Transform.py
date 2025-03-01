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

# Title
st.header("Discrete Fourier Transform (DFT)", divider=True)

st.markdown("""
The **Discrete Fourier Transform (DFT)** is a fundamental tool for frequency domain analysis of signals. 
It transforms a discrete-time sequence into its frequency components. The Fast Fourier Transform (FFT) 
optimizes this process using **butterfly operations**, significantly reducing computation time.
""")

# Butterfly Diagram Explanation
st.markdown("## Butterfly Diagram for FFT Computation")
st.markdown("""
The **Butterfly Diagram** is a graphical representation of the FFT algorithm. It helps visualize 
how the computation is structured in **Decimation-in-Time (DIT)** and **Decimation-in-Frequency (DIF)** approaches.
""")

# DIT-FFT Explanation
st.markdown("### Decimation-In-Time (DIT) FFT")
st.markdown("""
In **DIT-FFT**, the input sequence is rearranged in **bit-reversed order**, and the computation follows a hierarchical 
structure where smaller DFTs are combined using butterfly operations.

#### **4-Point DIT Butterfly Structure**
- The input is bit-reversed.
- Two stages of computation.
- Each butterfly involves **multiplication by twiddle factors**.

#### **8-Point DIT Butterfly Structure**
- Similar to the 4-point structure but with three stages.
- More computational savings using **symmetry properties**.
""")

# DIF-FFT Explanation
st.markdown("### Decimation-In-Frequency (DIF) FFT")
st.markdown("""
In **DIF-FFT**, the input remains in natural order, but the output gets bit-reversed. The computation starts by 
breaking down the signal into even and odd parts and applying butterfly operations.

#### **4-Point DIF Butterfly Structure**
- The first stage splits even and odd components.
- The second stage performs twiddle factor multiplication.

#### **8-Point DIF Butterfly Structure**
- More stages, leading to better computational efficiency.
- Uses the same butterfly structure as DIT but operates differently.
""")

# Applications of FFT
st.markdown("## Applications of FFT")
st.markdown("""
1. **Signal Processing** - Used in filtering, spectrum analysis, and audio compression.
2. **Image Processing** - Applied in JPEG and other image compression techniques.
3. **Wireless Communication** - Essential in OFDM modulation (used in 4G, 5G).
4. **Radar & Sonar Systems** - Helps in detecting objects using frequency shifts.
5. **Biomedical Signal Analysis** - Used in EEG, ECG frequency analysis.
""")

# Conclusion
st.markdown("## Conclusion")
st.markdown("""
The FFT algorithm optimizes DFT computation using butterfly diagrams, making it efficient for real-time applications. 
Understanding **DIT and DIF approaches** is crucial for designing high-speed digital signal processing systems.
""")

st.header("", divider="blue")

# Video options
video_options = {
    "4 Point DFT (DIT Type)": r"Media/4_pt_DFT_(DIT).mp4",
    "4 Point DFT (DIF Type)": r"Media/4_pt_DFT_(DIF).mp4",
    "8 Point DFT (DIT Type)": r"Media/8_pt_DFT_(DIT).mp4",
    "8 Point DFT (DIF Type)": r"Media/8_pt_DFT_(DIF).mp4",
}

# Dropdown to select video
selected_video = st.selectbox("Select DFT Video", list(video_options.keys()), index=0)

# Display selected video
st.video(video_options[selected_video])

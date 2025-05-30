import streamlit as st
import base64

# Set Streamlit page configuration
st.set_page_config(
    page_title="Signal Processing Virtual Lab",
    layout="wide",
    page_icon=" "  # Placeholder for page icon
)

# Inject custom CSS for scrollbar styling
st.markdown("""
    <style>
    /* Scrollbar track */
    ::-webkit-scrollbar {
        width: 16px;  
        height: 16px; 
    }

    /* Scrollbar thumb (the draggable part) */
    ::-webkit-scrollbar-thumb {
        background-color: #888;
        border-radius: 8px;
        border: 3px solid transparent;
        background-clip: content-box;
    }

    /* Scrollbar thumb on hover */
    ::-webkit-scrollbar-thumb:hover {
        background-color: #555;
    }

    /* Scrollbar track */
    ::-webkit-scrollbar-track {
        background: #f1f1f1;
    }
    </style>
""", unsafe_allow_html=True)

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

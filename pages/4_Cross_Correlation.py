import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import base64

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


st.header("Cross-Correlation", divider=True)

# Introduction
st.markdown("""
Cross-correlation is a fundamental technique in **signal processing** used to measure the similarity between two signals as a function of time lag.  
It is widely applied in **pattern recognition, noise reduction, and system identification**.
""")

# Key Features Section
st.header("Key Features")

# Cross-Correlation Definition
st.subheader("- Cross-Correlation Function")
st.markdown("The cross-correlation between two signals \\( x(t) \\) and \\( y(t) \\) is defined as:")
st.latex(r"R_{xy}(\tau) = \int_{-\infty}^{\infty} x(t) y(t - \tau) dt")

st.markdown("""
- It is useful in **signal alignment, detection, and feature extraction**.
""")

# Graphical Analysis
st.subheader("- Graphical Analysis of Cross-Correlation")
st.markdown("""
- Compute and visualize **cross-correlation** for **sinusoidal (sine, cosine) and square waveforms**.  
- Analyze how signals correlate when mixed with **noisy versions** of themselves.  
- Identify **signal patterns, delay estimation, and filtering performance**.  
""")

# Applications
st.subheader("- Applications")
st.markdown("""
- **Noise Filtering**: Identifying and removing noise from signals.  
- **Synchronization**: Estimating time delay between received and transmitted signals.  
- **Feature Detection**: Recognizing repeating patterns in data.  
""")

# Conclusion
st.markdown("""
This tool is essential for **engineers, researchers, and students** in **communications, radar systems, audio processing, and biomedical signal analysis**.
""")

st.header("", divider="blue")

# Function to generate signals
def generate_signal(signal_type, t):
    frequency = 5  # Frequency of the wave
    if signal_type == 'Sin':
        return np.sin(2 * np.pi * frequency * t)
    elif signal_type == 'Cos':
        return np.cos(2 * np.pi * frequency * t)
    elif signal_type == 'Square':
        return np.sign(np.sin(2 * np.pi * frequency * t))
    else:
        return np.zeros_like(t)

# Function to compute cross-correlation
def cross_correlation(x, y):
    n = len(x)
    mean_x = np.mean(x)
    mean_y = np.mean(y)
    x_centered = x - mean_x
    y_centered = y - mean_y
    correlation = np.correlate(x_centered, y_centered, mode='full')
    return correlation / (n * np.std(x) * np.std(y))

# Streamlit UI

signal_choice = st.selectbox("Function :", ["Sin", "Cos", "Square"])

if st.button("Plot"):
    t = np.linspace(0, 1, 1000)  # 1 second duration with 1000 samples
    signal1 = generate_signal(signal_choice, t)
    noise = np.random.normal(0, 0.5, signal1.shape)
    signal2 = signal1 + noise
    corr_result = cross_correlation(signal1, signal2)
    lags = np.arange(-len(signal1) + 1, len(signal1))
    
    fig, axs = plt.subplots(3, 1, figsize=(13, 15))
    
    axs[0].plot(t, signal1, color='darkblue')
    axs[0].set_title(f'Original {signal_choice.capitalize()} Signal')
    axs[0].grid()
    
    axs[1].plot(t, signal2, color='red')
    axs[1].set_title('Noisy Signal')
    axs[1].grid()
    
    axs[2].plot(lags, corr_result, color='darkgreen')
    axs[2].set_title('Cross-Correlation Result')
    axs[2].set_xlabel('Lags')
    axs[2].set_ylabel('Cross-Correlation')
    axs[2].grid()
    
    st.pyplot(fig)

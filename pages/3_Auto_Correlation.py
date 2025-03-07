import numpy as np
import matplotlib.pyplot as plt
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


# Streamlit UI
st.header("Autocorrelation & ESD", divider=True)

st.markdown("""
**Autocorrelation & ESD** enables the **graphical analysis** of **Auto-correlation** and **Energy Spectral Density (ESD)** for fundamental signal types, including **Sine, Cosine, and Square signals**. These techniques are essential in **signal processing, communications, and spectral analysis**.
""")



# Auto-correlation Function
st.subheader("- Auto-correlation Function")
st.markdown("""
Auto-correlation measures the similarity between a signal and a time-shifted version of itself. It is defined as:

$$
R_x(\tau) = \int_{-\infty}^{\infty} x(t) x(t - \tau) dt
$$

- Helps identify periodicity and signal similarity.
- Used in **noise reduction, pattern recognition, and signal analysis**.
- **Auto-correlation and ESD** are visualized for **Sine, Cosine, and Square signals**.  
""")

# Energy Spectral Density (ESD)
st.subheader("- Energy Spectral Density (ESD)")
st.markdown("""
The **Energy Spectral Density (ESD)** represents the energy distribution of a signal in the frequency domain. It is obtained using the Fourier Transform of the auto-correlation function:

$$
S_x(f) = \mathcal{F} \{ R_x(\tau) \}
$$

- Provides insight into the **frequency components** of a signal.
- Essential for **signal power analysis, filter design, and system modeling**.
""")

# Conclusion
st.markdown("""
This tool is highly useful for **engineers, researchers, and students** involved in **signal analysis, wireless communication, and control systems**.
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

# Function to compute autocorrelation
def autocorrelation(x):
    n = len(x)
    mean_x = np.mean(x)
    x_centered = x - mean_x  # Normalize the signal
    correlation = np.correlate(x_centered, x_centered, mode='full')
    return correlation / (n * np.var(x))

# Function to compute ESD
def calculate_esd(signal, t):
    fft_result = np.fft.fft(signal)
    esd = (np.abs(fft_result) ** 2) / len(signal)
    freqs = np.fft.fftfreq(len(signal), d=t[1] - t[0])
    return freqs[:len(freqs) // 2], esd[:len(esd) // 2]


signal_choice = st.selectbox("Function Type :", ["Sin", "Cos", "Square"])

if st.button("Plot"):
    t = np.linspace(0, 1, 1000)  # 1 second duration with 1000 samples
    signal1 = generate_signal(signal_choice, t)
    noise = np.random.normal(0, 0.5, signal1.shape)
    signal2 = signal1 + noise

    auto_corr_signal1 = autocorrelation(signal1)
    auto_corr_signal2 = autocorrelation(signal2)
    lags = np.arange(-len(signal1) + 1, len(signal1))

    freqs, esd_noisy = calculate_esd(signal2, t)

    fig, axs = plt.subplots(4, 1, figsize=(10, 20))
    axs[0].plot(t, signal1, color='darkblue')
    axs[0].set_title(f'Original {signal_choice.capitalize()} Wave Signal')
    axs[0].grid()
    
    axs[1].plot(t, signal2, color='red')
    axs[1].set_title('Noisy Signal')
    axs[1].grid()
    
    axs[2].plot(lags, auto_corr_signal1, label='Clean Signal', color='darkblue')
    axs[2].plot(lags, auto_corr_signal2, label='Noisy Signal', color='red')
    axs[2].set_title('Autocorrelation Results')
    axs[2].set_xlabel('Lags')
    axs[2].legend()
    axs[2].grid()
    
    axs[3].plot(freqs, esd_noisy, color='magenta')
    axs[3].set_xlim(0, 3 * 5)  # Limit frequency axis
    axs[3].set_ylim(0, np.max(esd_noisy) * 1.1)
    axs[3].set_title('Energy Spectral Density (ESD) of Noisy Signal')
    axs[3].set_xlabel('Frequency (Hz)')
    axs[3].set_ylabel('Energy Spectral Density')
    axs[3].grid()
    
    st.pyplot(fig)

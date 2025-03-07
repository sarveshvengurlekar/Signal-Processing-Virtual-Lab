import numpy as np
import matplotlib.pyplot as plt
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

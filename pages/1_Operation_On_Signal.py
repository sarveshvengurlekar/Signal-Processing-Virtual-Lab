import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq
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
st.markdown(hide_menu, unsafe_allow_html=True)

st.header("Operations on Signal", divider=True)


st.markdown("""
**The Operation on Signal** enables advanced signal operations by allowing users to generate and manipulate various waveforms, including **Sine , Cosine, & Square waves**. Users can dynamically control signal **amplitude and frequency**, facilitating precise waveform synthesis.
""")

# Waveform Selection & Parameter Control
st.subheader("- Waveform Selection & Parameter Control")
st.markdown("""
- Choose from **sinusoidal, cosine, and square waveforms**.  
- Adjust **amplitude (A)** and **frequency (f)** in real time for signal tuning.  
""")

# Mathematical Signal Operations
st.subheader("- Mathematical Signal Operations")
st.markdown("""
- **Addition**: Combine multiple signals to generate complex waveforms.  
- **Subtraction**: Analyze the difference between two signals.  
- **Multiplication**: Perform amplitude modulation and other signal processing tasks.  
""")

# Frequency Spectrum Analysis
st.subheader("- Frequency Spectrum Analysis")
st.markdown("""
- Visualize signals in both the **time domain** and **frequency domain**.  
- Utilize **Fourier Transform techniques** to analyze spectral components.  
""")

# Conclusion
st.markdown("""
This system is ideal for applications in **signal processing, telecommunications, and waveform analysis**, offering an intuitive yet powerful environment for engineers, researchers, and students.
""")

st.header("", divider="blue")

def generate_signal(t, amplitude, frequency, func_type, phase_shift):
    # Function to generate the signals based on the selected function
    if func_type == "Sin":
        return amplitude * np.sin(2 * np.pi * frequency * t + phase_shift)
    elif func_type == "Cos":
        return amplitude * np.cos(2 * np.pi * frequency * t + phase_shift)
    elif func_type == "Square":
        return amplitude * np.sign(np.sin(2 * np.pi * frequency * t + phase_shift))
    else:
        return np.zeros_like(t)

def handle_selection():
    # Options for dropdown menus
    Amp_option = [5.0, 10.0, 20.0, 30.0]
    Freq_option = [30.0, 40.0, 50.0, 60.0]
    Phase_option = [0.0, 1.0, 2.0, 3.0, 4.0]
    Time_option = [1.0, 2.0, 3.0, 4.0, 5.0]
    num_points = 1000

    # Creating GUI
    col1, col2 = st.columns(2)
    with col1:
        Amp_selection_1 = st.number_input("Amplitude 1:", value=Amp_option[0], step=5.0, format="%.1f")
        Freq_selection_1 = st.number_input("Frequency 1 (Hz):", value=Freq_option[0], step=5.0, format="%.1f")
        Phase_selection_1 = st.number_input("Phase Shift 1 (Rad/sec):", value=Phase_option[0], step=1.0, format="%.1f")
        Function_selection_1 = st.selectbox("Function 1:", ("Sin", "Cos", "Square"))
    with col2:
        Amp_selection_2 = st.number_input("Amplitude 2:", value=Amp_option[0], step=5.0, format="%.1f")
        Freq_selection_2 = st.number_input("Frequency 2 (Hz):", value=Freq_option[0], step=5.0, format="%.1f")
        Phase_selection_2 = st.number_input("Phase Shift 2 (Rad/sec):", value=Phase_option[0], step=1.0, format="%.1f")
        Function_selection_2 = st.selectbox("Function 2:", ("Sin", "Cos", "Square"))

    Time_Duration = st.number_input("Time Duration (Sec.):", value=Time_option[0], step=1.0, format="%.1f")
    Operation_selection = st.selectbox("Operation:", ("Addition", "Subtraction", "Multiplication"))

    # Time array for the signals
    t = np.linspace(0, Time_Duration, num_points)
    
    # Create the signals based on the selected parameters
    signal_1 = generate_signal(t, Amp_selection_1, Freq_selection_1, Function_selection_1, Phase_selection_1)
    signal_2 = generate_signal(t, Amp_selection_2, Freq_selection_2, Function_selection_2, Phase_selection_2)

    # Perform the selected operation
    if Operation_selection == "Addition":
        result_signal = signal_1 + signal_2
    elif Operation_selection == "Subtraction":
        result_signal = signal_1 - signal_2
    elif Operation_selection == "Multiplication":
        result_signal = signal_1 * signal_2

    return t, signal_1, signal_2, result_signal

def plotting_signal(t, signal_1, signal_2, result_signal):
    N = len(t)
    T = t[1] - t[0]
    xf = fftfreq(N, T)[:N//2]
    yf_1 = fft(signal_1)
    yf_2 = fft(signal_2)
    yf_result = fft(result_signal)

    fig, axes = plt.subplots(3, 2, figsize=(10, 8))
    axes[0, 0].plot(t, signal_1, color='darkblue')
    axes[0, 0].set_title("Signal 1")
    axes[0, 1].plot(xf, 2.0/N * np.abs(yf_1[:N//2]), color='darkblue')
    axes[0, 1].set_title("Frequency Spectrum of Signal 1")
    
    axes[1, 0].plot(t, signal_2, color='orangered')
    axes[1, 0].set_title("Signal 2")
    axes[1, 1].plot(xf, 2.0/N * np.abs(yf_2[:N//2]), color='orangered')
    axes[1, 1].set_title("Frequency Spectrum of Signal 2")
    
    axes[2, 0].plot(t, result_signal, color='green')
    axes[2, 0].set_title("Result Signal")
    axes[2, 1].plot(xf, 2.0/N * np.abs(yf_result[:N//2]), color='green')
    axes[2, 1].set_title("Frequency Spectrum of Result Signal")
    
    plt.tight_layout()
    st.pyplot(fig)

t, signal_1, signal_2, result_signal = handle_selection()
if st.button("Plot"):
    plotting_signal(t, signal_1, signal_2, result_signal)

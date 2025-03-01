import numpy as np
import scipy.signal as signal
import scipy.io.wavfile as wav
import soundfile as sf
import streamlit as st
import matplotlib.pyplot as plt
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

# Streamlit app title
st.header("LTI System", divider=True)

st.markdown("""
### Linear Time-Invariant (LTI) Systems and Audio Processing

In signal processing, **Linear Time-Invariant (LTI) Systems** are systems where the output is a linear function of the input, and their properties do not change over time. These systems are characterized by their **impulse response**, \( h(t) \), which determines how the system responds to any given input.

The general equation for an LTI system is:

$$
y(t) = \int_{-\infty}^{\infty} h(\tau) x(t-\tau) d\tau
$$

where:
- \( y(t) \) is the output signal,
- \( x(t) \) is the input signal,
- \( h(t) \) is the impulse response.

### Filters in LTI Systems

Two common types of filters used in LTI systems are **Low-Pass Filters (LPF)** and **High-Pass Filters (HPF)**.

#### Low-Pass Filter (LPF)

A Low-Pass Filter allows signals with frequencies below a certain cutoff frequency \( f_c \) to pass through, while attenuating higher frequencies.
#### High-Pass Filter (HPF)

A High-Pass Filter allows signals with frequencies above a certain cutoff frequency \( f_c \) to pass through, while attenuating lower frequencies.

### Application in Audio Processing

LTI systems can be applied to real-time audio input to filter and modify the signal. In this Streamlit application, you can:

1. **Input Audio:** Upload an audio file to process.
2. **Select Filter:** Choose between a Low-Pass or High-Pass filter.
3. **Adjust Filter Parameters:** Set the cutoff frequency for the selected filter.
4. **Output Processed Audio:** The filtered audio is processed and played back.

This process allows you to observe how different filters affect the frequency spectrum and overall quality of the audio signal.

#### Example: Effect of Low-Pass Filter

A Low-Pass Filter with a cutoff frequency of \( 500 \, \text{Hz} \) would attenuate frequencies above \( 500 \, \text{Hz} \), allowing only the lower frequencies to pass. This would be useful for removing high-frequency noise from a recording.

#### Example: Effect of High-Pass Filter

A High-Pass Filter with a cutoff frequency of \( 50 \, \text{Hz} \) would block any frequencies below \( 50 \, \text{Hz} \), making it ideal for removing low-frequency hums or rumble.

---

You can experiment with different filters and audio inputs to better understand the impact of LTI systems on audio signals.
""")


# File uploader
uploaded_file = st.file_uploader("Upload a WAV file", type=["wav"])

# Global variables
audio = None
sample_rate = None
filtered_audio = None
filter_params = None

if uploaded_file is not None:
    sample_rate, audio = wav.read(uploaded_file)
    
    # Convert stereo to mono if needed
    if audio.ndim > 1:
        audio = np.mean(audio, axis=1)
    
    # Normalize audio
    audio = audio / np.max(np.abs(audio))
    
    st.audio(uploaded_file, format='audio/wav')
    st.success("Audio file loaded successfully!")

    # Filter selection
    filter_type = st.selectbox("Select Filter Type", ["Low-Pass", "High-Pass"])
    nyquist = 0.5 * sample_rate
    
    # Cutoff frequency inputs
    if filter_type in ["Low-Pass", "High-Pass"]:
        cutoff = st.number_input("Cutoff Frequency (Hz)", min_value=1, max_value=int(nyquist)-1, step=1)
    # Apply filter button
    if st.button("Apply Filter"):
        try:
            if filter_type == "Low-Pass":
                normal_cutoff = cutoff / nyquist
                b, a = signal.butter(6, normal_cutoff, btype='low', analog=False)
            elif filter_type == "High-Pass":
                normal_cutoff = cutoff / nyquist
                b, a = signal.butter(6, normal_cutoff, btype='high', analog=False)
            
            # Apply filter
            filtered_audio = signal.filtfilt(b, a, audio)
            filter_params = (b, a)
            
            # Save filtered audio as WAV
            sf.write("filtered_audio.wav", filtered_audio, sample_rate)
            st.success("Filter applied! You can now play the filtered audio.")
            st.audio("filtered_audio.wav", format='audio/wav')
        except ValueError:
            st.error("Invalid input! Please enter valid numeric cutoff values.")
    
    # Plot frequency response
    if filter_params is not None:
        if st.button("Plot Frequency Response"):
            b, a = filter_params
            w, h = signal.freqz(b, a, worN=2000)
            fig, ax = plt.subplots(figsize=(8, 6))
            ax.plot(w * nyquist / np.pi, 20 * np.log10(abs(h)), 'black')
            ax.set_title("Filter Frequency Response")
            ax.set_xlabel("Frequency (Hz)")
            ax.set_ylabel("Gain (dB)")
            ax.grid(color='gray', linestyle='--', linewidth=0.5)
            st.pyplot(fig)

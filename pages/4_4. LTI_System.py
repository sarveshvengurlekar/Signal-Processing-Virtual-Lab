import base64
import streamlit as st
import numpy as np
import scipy.signal as signal
import scipy.io.wavfile as wav
import io
import matplotlib.pyplot as plt


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
        <p>© Fr. Conceicao Rodrigues Institute of Technology. All rights reserved.</p>
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

A Low-Pass Filter with a cutoff frequency of \( 500 \, Hz \) would attenuate frequencies above \( 500 \, Hz \), allowing only the lower frequencies to pass. This would be useful for removing high-frequency noise from a recording.

#### Example: Effect of High-Pass Filter

A High-Pass Filter with a cutoff frequency of \( 50 \, Hz} \) would block any frequencies below \( 50 \, Hz \), making it ideal for removing low-frequency hums or rumble.

local_file_path = "Media/LTI_Audio.wav"  # Update this with the correct path

# Read the file in binary mode
with open(local_file_path, "rb") as file:
    wav_bytes = file.read()
    # Streamlit download button

st.download_button(
    label="Download Audio File",
    data=wav_bytes,
    file_name="LTI_Audio.wav",
    mime="audio/wav")

---

""")


# Function to convert audio to base64 for browser playback
def get_audio_base64(audio, sample_rate):
    buffer = io.BytesIO()
    wav.write(buffer, sample_rate, (audio * 32767).astype(np.int16))
    audio_bytes = buffer.getvalue()
    audio_base64 = base64.b64encode(audio_bytes).decode()
    return f"data:audio/wav;base64,{audio_base64}"

# Initialize session state variables
if 'audio' not in st.session_state:
    st.session_state.audio = None
    st.session_state.sample_rate = None
    st.session_state.filtered_audio = None
    st.session_state.filter_params = None

# Streamlit app layout
#st.title("Audio Filtering App")

# File uploader
uploaded_file = st.file_uploader("Upload a WAV file", type=["wav"])

if uploaded_file is not None:
    try:
        # Read and process audio file
        sample_rate, audio = wav.read(uploaded_file)
        if audio.ndim > 1:
            audio = np.mean(audio, axis=1)
        audio = audio / np.max(np.abs(audio))
        st.session_state.audio = audio
        st.session_state.sample_rate = sample_rate
        st.success("Audio file loaded successfully!")
        
        # Display original audio
        st.audio(get_audio_base64(audio, sample_rate), format="audio/wav")
        
    except Exception as e:
        st.error(f"Failed to load audio: {e}")

# Filter selection
filter_type = st.selectbox("Select Filter Type", ["Low-Pass", "High-Pass"])

# Cutoff frequency inputs
nyquist = 0.5 * st.session_state.sample_rate if st.session_state.sample_rate else 22050  # Default Nyquist for error handling
col1, col2 = st.columns(2)

if filter_type in ["Low-Pass", "High-Pass"]:
    cutoff = col1.number_input("Cutoff Frequency (Hz)", min_value=1, max_value=int(nyquist), value=1000)
elif filter_type == "Band-Pass":
    low_cutoff = col1.number_input("Lower Cutoff Frequency (Hz)", min_value=1, max_value=int(nyquist), value=500)
    high_cutoff = col2.number_input("Upper Cutoff Frequency (Hz)", min_value=1, max_value=int(nyquist), value=1500)

# Apply filter button
if st.button("Apply Filter"):
    if st.session_state.audio is None:
        st.error("No audio file loaded!")
    else:
        try:
            if filter_type == "Low-Pass":
                normal_cutoff = cutoff / nyquist
                b, a = signal.butter(6, normal_cutoff, btype='low', analog=False)
            elif filter_type == "High-Pass":
                normal_cutoff = cutoff / nyquist
                b, a = signal.butter(6, normal_cutoff, btype='high', analog=False)
            elif filter_type == "Band-Pass":
                if low_cutoff >= high_cutoff or low_cutoff <= 0 or high_cutoff >= nyquist:
                    st.error(f"Enter valid frequencies (1-{int(nyquist)} Hz) with low < high.")
                else:
                    normal_cutoff = [low_cutoff / nyquist, high_cutoff / nyquist]
                    b, a = signal.butter(6, normal_cutoff, btype='band', analog=False)
            
            # Apply filter
            st.session_state.filtered_audio = signal.filtfilt(b, a, st.session_state.audio)
            st.session_state.filter_params = (b, a)
            st.success("Filter applied! You can now play the filtered audio or plot the response.")
            
            # Display filtered audio
            st.audio(get_audio_base64(st.session_state.filtered_audio, st.session_state.sample_rate), format="audio/wav")
            
        except ValueError:
            st.error("Invalid input! Please enter valid numeric cutoff values.")

# Plot response button
if st.button("Plot Response"):
    if st.session_state.filter_params is None:
        st.error("Apply a filter first to plot the response!")
    else:
        b, a = st.session_state.filter_params
        nyquist = 0.5 * st.session_state.sample_rate
        w, h = signal.freqz(b, a, worN=2000)

        # Compute FFT
        N = len(st.session_state.audio)
        N_fft = 2**np.ceil(np.log2(N)).astype(int)
        freqs = np.fft.fftfreq(N_fft, d=1/st.session_state.sample_rate)
        fft_original = np.fft.fft(st.session_state.audio, N_fft)
        fft_filtered = np.fft.fft(st.session_state.filtered_audio, N_fft) if st.session_state.filtered_audio is not None else None

        # Set x-axis range
        max_freq = min(5000, nyquist)
        mask = (freqs >= 0) & (freqs <= max_freq)
        freq_hz = freqs[mask]
        filter_freq_hz = (w * nyquist / np.pi)

        # Create plots
        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 8))

        # Filter Frequency Response
        ax1.plot(filter_freq_hz, 20 * np.log10(abs(h)), 'black')
        ax1.set_title("Filter Frequency Response")
        ax1.set_xlabel("Frequency (Hz)")
        ax1.set_ylabel("Gain (dB)")
        ax1.set_xticks(np.arange(250, max_freq+1, 250))
        ax1.set_xlim(0, max_freq)
        ax1.grid(color='gray', linestyle='--', linewidth=0.5)

        # FFT of Original Audio
        ax2.plot(freq_hz, np.abs(fft_original[mask]), color='blue')
        ax2.set_title("FFT of Original Audio")
        ax2.set_xlabel("Frequency (Hz)")
        ax2.set_ylabel("Magnitude")
        ax2.set_xticks(np.arange(250, max_freq+1, 250))
        ax2.set_xlim(0, max_freq)
        ax2.grid(color='gray', linestyle='--', linewidth=0.5)

        # FFT of Filtered Audio
        if fft_filtered is not None:
            ax3.plot(freq_hz, np.abs(fft_filtered[mask]), color='red')
            ax3.set_title("FFT of Filtered Audio")
            ax3.set_xlabel("Frequency (Hz)")
            ax3.set_ylabel("Magnitude")
            ax3.set_xticks(np.arange(250, max_freq+1, 250))
            ax3.set_xlim(0, max_freq)
            ax3.grid(color='gray', linestyle='--', linewidth=0.5)

        plt.tight_layout()
        st.pyplot(fig)

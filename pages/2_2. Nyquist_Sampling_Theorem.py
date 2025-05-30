import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import wave
import base64
from scipy.signal import resample
import soundfile as sf
import io
import wave

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

st.header("Nyquist Sampling Theorem", divider=True)

st.markdown("""
The **Nyquist Sampling Theorem** is a fundamental principle in **signal processing** that defines the minimum sampling rate required to accurately reconstruct a continuous-time signal from its samples.  
This theorem plays a crucial role in **digital audio, communications, and data acquisition systems**.
""")

# Nyquist Theorem Definition
st.subheader("- Nyquist Sampling Theorem")
st.markdown("The theorem states that a band-limited signal with a maximum frequency component of must be sampled at a rate of at least **twice its highest frequency** to ensure perfect reconstruction:")

st.latex(r"f_s \geq 2 f_{max}")

st.markdown("""
The Failure to satisfy this condition results in **aliasing**, where high-frequency components appear as low-frequency distortions.
""")

# Graphical & Audible Analysis
st.subheader("- Real-Time Analysis")
st.markdown("""
- **Graphical Visualization:** Observe the effects of **under-sampling, proper sampling, and over-sampling** in real-time.  
- **Audible Feedback:** Hear the reconstructed audio at different sampling rates to understand the impact on sound quality.  
""")

# Applications
st.subheader("- Applications")
st.markdown("""
- **Digital Audio Processing**: Ensures high-fidelity sound reproduction.  
- **Telecommunications**: Prevents signal distortion in data transmission.  
- **Medical Imaging**: Used in MRI and CT scan reconstruction.  
- **Radar & Sonar**: Optimizes signal detection and tracking.
""")

# Conclusion
st.markdown("""
This tool is valuable for **engineers, researchers, and students** in **signal processing, telecommunications, and real-time system design**.
""")

# Define the local file path
local_file_path = "Media/audio2 (2).wav"  # Update this with the correct path

# Read the file in binary mode
with open(local_file_path, "rb") as file:
    wav_bytes = file.read()
    # Streamlit download button

st.download_button(
    label="Download Audio File",
    data=wav_bytes,
    file_name="Sampling_audio.wav",
    mime="audio/wav")

st.header("",divider="blue")


# Sidebar: Choose input method
st.header("Input Signal")
input_method = st.selectbox("Select Signal Source", ["Generate Tone", "Upload Audio File (.wav)"])

# Function to convert numpy audio to WAV
def convert_to_wav(audio_array, sample_rate):
    wav_buffer = io.BytesIO()
    with wave.open(wav_buffer, 'wb') as wf:
        wf.setnchannels(1)  # Mono audio
        wf.setsampwidth(2)  # 16-bit PCM
        wf.setframerate(sample_rate)
        wf.writeframes((audio_array * 32767).astype(np.int16).tobytes())
    return wav_buffer.getvalue()

# Initialize variables
audio_data = None
sample_rate = 44100  # Default sample rate

# Handle audio file upload
if input_method == "Upload Audio File (.wav)":
    upload_file = st.file_uploader("Upload an audio file (WAV)", type=["wav"])

    if upload_file:
        audio_data, sample_rate = sf.read(upload_file)
        if audio_data.ndim > 1:
            audio_data = np.mean(audio_data, axis=1)  # Convert to mono
            st.write(f"Original Sampling Rate: {sample_rate} Hz")

# Handle sine wave generation
elif input_method == "Generate Tone":
    st.header("Tone Generator")
    frequency = st.number_input("Tone Frequency (Hz)", 50, 8000, 2500)
    duration = st.slider("Duration (seconds)", 1, 5, 2)
    sample_rate = 44100
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    audio_data = 0.5 * np.sin(2 * np.pi * frequency * t)
    st.write(f"Generated Tone: Sine |{frequency} Hz | {duration} sec")

# Function to calculate maximum frequency using FFT
def get_max_frequency(audio_data, sample_rate):
    N = len(audio_data)
    fft_data = np.fft.fft(audio_data)
    fft_freqs = np.fft.fftfreq(N, 1 / sample_rate)
    positive_freqs = fft_freqs[:N // 2]
    positive_fft_data = np.abs(fft_data[:N // 2])
    max_freq_idx = np.argmax(positive_fft_data)
    return positive_freqs[max_freq_idx]

if audio_data is not None:
    max_freq = get_max_frequency(audio_data, sample_rate)
    st.write(f"Maximum Frequency Component: {max_freq:.2f} Hz")

    # Add original audio playback
    st.subheader("Original Audio")
    st.write("🔊 Original Signal")
    st.audio(convert_to_wav(audio_data, sample_rate), format="audio/wav")

    # Sampling parameters
    default_Fs_under = int(max_freq / 1.5)  # Undersampling (Aliasing)
    default_Fs_critical = int(max_freq)  # Critical sampling
    default_Fs_over = int(2.5 * max_freq)  # Oversampling (No Aliasing)

    Fs_under = st.number_input("Undersampling Frequency (Fs < Fm)", min_value=1, value=default_Fs_under)
    Fs_critical = st.number_input("Critical Sampling Frequency (Fs = Fm)", min_value=1, value=default_Fs_critical)
    Fs_over = st.number_input("Oversampling Frequency (Fs > 2Fm)", min_value=1, value=default_Fs_over)
    
    sampling_rates = [Fs_under, Fs_critical, Fs_over]
    titles = ["Undersampling (Aliasing)", "Critical Sampling", "Oversampling (No Aliasing)"]
    colors = ["red", "orange", "darkblue"]

    # Play reconstructed audio (before the plots)
    st.subheader("Reconstructed Audio")
    for i, Fs in enumerate(sampling_rates):
        sample_indices = np.arange(0, len(audio_data), sample_rate // Fs)
        sampled_signal = audio_data[sample_indices]
        reconstructed_signal = np.interp(np.arange(len(audio_data)), sample_indices, sampled_signal)
        st.write(f"🔊 {titles[i]} (Fs = {Fs} Hz)")
        st.audio(convert_to_wav(reconstructed_signal, sample_rate), format="audio/wav")

    # Function to plot time-domain signal
    def plot_time_domain(audio_signal, sample_rate, title, ax, color):
        N = min(1500, len(audio_signal))  # Only first 1500 samples
        t = np.linspace(0, N / sample_rate, num=N)
        ax.plot(t, audio_signal[:N], color=color)
        ax.set_xlabel("Time (s)")
        ax.set_ylabel("Amplitude")
        ax.set_title(title)

    # Function to plot frequency spectrum
    def plot_frequency_spectrum(audio_signal, sample_rate, title, ax, color):
        N = len(audio_signal)
        fft_data = np.fft.fft(audio_signal)
        fft_freqs = np.fft.fftfreq(N, 1 / sample_rate)
        positive_freqs = fft_freqs[:N // 2]
        positive_fft_data = np.abs(fft_data[:N // 2])
        ax.plot(positive_freqs, positive_fft_data, color=color)
        ax.set_xlabel("Frequency (Hz)")
        ax.set_ylabel("Magnitude")
        ax.set_title(title)
        ax.set_xlim(0, sample_rate / 2)

    # Create 4x2 Subplots (Time Domain & Frequency Domain)
    fig, axs = plt.subplots(4, 2, figsize=(16, 16))

    # Original Signal (Time Domain & Frequency Domain)
    plot_time_domain(audio_data, sample_rate, "Original Signal (Time Domain)", axs[0, 0], "darkviolet")
    plot_frequency_spectrum(audio_data, sample_rate, "Original Signal Spectrum", axs[0, 1], "darkviolet")

    # Plot sampled signal (Time domain & Frequency domain)
    for i, Fs in enumerate(sampling_rates):
        sample_indices = np.arange(0, len(audio_data), sample_rate // Fs)
        sampled_signal = audio_data[sample_indices]
        reconstructed_signal = np.interp(np.arange(len(audio_data)), sample_indices, sampled_signal)

        # Time-domain plots (left column)
        plot_time_domain(reconstructed_signal, sample_rate, f"{titles[i]} (Time Domain)", axs[i+1, 0], colors[i])

        # Frequency-domain plots (right column)
        plot_frequency_spectrum(reconstructed_signal, sample_rate, f"{titles[i]} Spectrum", axs[i+1, 1], colors[i])

    # Adjust layout and display plot at the end
    plt.tight_layout()
    st.pyplot(fig)


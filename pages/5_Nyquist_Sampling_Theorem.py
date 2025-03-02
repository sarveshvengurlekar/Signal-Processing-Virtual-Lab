import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import wave
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

st.header("",divider="blue")

def is_wav_file(file_path):
    """Check if the file is a valid WAV file."""
    try:
        with wave.open(file_path, 'rb') as wav_file:
            return True
    except (wave.Error, FileNotFoundError):
        return False

def modify_sampling_rate(data, original_rate, new_rate):
    """Resample the audio signal."""
    duration = len(data) / original_rate
    new_length = int(duration * new_rate)
    modified_data = np.interp(
        np.linspace(0, len(data) - 1, new_length),
        np.arange(len(data)),
        data
    ).astype(data.dtype)
    return modified_data

def save_wav(filename, data, samplerate):
    """Save the modified WAV file."""
    with wave.open(filename, 'wb') as wav_file:
        wav_file.setnchannels(1)  # Mono
        wav_file.setsampwidth(2)
        wav_file.setframerate(samplerate)
        wav_file.writeframes((data * 32767).astype(np.int16).tobytes())

uploaded_file = st.file_uploader("Upload an Audio File (.wav)", type=["wav"])
if uploaded_file:
    file_path = f"temp_{uploaded_file.name}"
    
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    if is_wav_file(file_path):
        with wave.open(file_path, 'rb') as wav_file:
            samplerate = wav_file.getframerate()
            num_frames = wav_file.getnframes()
            audio_data = np.frombuffer(wav_file.readframes(num_frames), dtype=np.int16)

        st.write(f"Original Sampling Rate: {samplerate} Hz")

        new_rate = st.number_input("Enter New Sampling Rate (Hz):", min_value=100, max_value=50000, value=samplerate, step=100)
        
        if st.button("Play Original"):
            st.audio(file_path, format="audio/wav")

        if st.button("Process & Play Modified"):
            modified_data = modify_sampling_rate(audio_data, samplerate, new_rate)
            output_filename = "processed_audio.wav"
            save_wav(output_filename, modified_data, new_rate)
            
            st.audio(output_filename, format="audio/wav")

    else:
        st.error("The selected file is not a valid .wav file.")

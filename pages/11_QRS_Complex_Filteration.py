import scipy.io
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import butter, filtfilt
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
logo_path = r"C:\Users\sarve\Downloads\Coding\Python\DSP Internship\Streamlit\Signals & System Virtual Lab\static\fcritlogo.png"
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

# Streamlit UI to select .mat file
st.header("QRS Complex Filteration",divider=True)

st.markdown("""
The **QRS complex** is a crucial component of an Electrocardiogram (ECG) signal, representing ventricular 
depolarization. However, real-world ECG signals often contain noise from sources like muscle artifacts, baseline 
wandering, and power-line interference. To accurately detect and analyze the QRS complex, **signal filtering** is necessary.
""")

# Noise in ECG Signals
st.markdown("## Sources of Noise in ECG Signals")
st.markdown("""
1. **Baseline Wander** – Low-frequency variations due to respiration and electrode movement.
2. **Power-Line Interference** – 50/60 Hz noise from electrical sources.
3. **Muscle Artifacts (EMG Noise)** – High-frequency components from muscle contractions.
4. **Motion Artifacts** – Sudden shifts in baseline due to patient movement.
""")

# QRS Filtration Methods
st.markdown("## Methods for QRS Complex Filtration")
st.markdown("""
To remove noise while preserving the QRS complex, the following filtering techniques are commonly used:

- **Bandpass Filtering (0.5 - 45 Hz):** Removes baseline wander and high-frequency artifacts.
- **Notch Filtering (50/60 Hz):** Suppresses power-line interference.
- **Wavelet Denoising:** Uses multi-resolution decomposition to isolate QRS components.
- **Adaptive Filtering:** Adjusts filter coefficients in real-time to improve accuracy.
""")

# Importance of Filtration
st.markdown("## Importance of QRS Complex Filtration")
st.markdown("""
Filtering the QRS complex ensures precise feature extraction for:
- **Arrhythmia detection**
- **Heart rate variability (HRV) analysis**
- **Automatic ECG classification in medical diagnostics**
""")

# Conclusion
st.markdown("## Conclusion")
st.markdown("""
Efficient filtration techniques are essential to enhance ECG signal quality and enable accurate QRS detection. 
Combining multiple filtering approaches leads to optimal performance in real-time and offline ECG analysis.
""")

st.header("", divider="blue")


uploaded_file = st.file_uploader("ECG File (.mat) :", type=["mat"])

if uploaded_file is not None:
    try:
        data = scipy.io.loadmat(uploaded_file)
        st.success(".mat file loaded successfully!")
    except Exception as e:
        st.error(f"Failed to load .mat file: {e}")
        st.stop()
    
    # Inspect the .mat file to find the variable containing the ECG signal
    try:
        ecq_key = [key for key in data.keys() if not key.startswith('__')][0]
        ecq_signal_1 = data[ecq_key]  # Use the detected key
        
        if ecq_signal_1.ndim > 1:
            ecq_signal_1 = ecq_signal_1.flatten()
    except Exception as e:
        st.error(f"Error processing ECG signal from .mat file: {e}")
        st.stop()
    
    # Define sampling frequency (Hz)
    fs = 250  # Example: Sampling frequency in Hz
    
    # Create time vector for plotting
    time = np.arange(len(ecq_signal_1)) / fs
    
    # Find the location of the R-peak (for simplicity, assuming a rough peak here)
    cycle_start = 500  # For example, assume the cycle starts at index 500
    cycle_end = cycle_start + int(fs * 1.0)  # Assuming 1 second for one cycle (adjust if needed)
    
    # Extract one cycle from the ECG signal
    ecq_cycle = ecq_signal_1[cycle_start:cycle_end]
    
    # Generate a noisy version of the extracted cycle
    ecq_cycle_noisy = ecq_cycle + np.random.normal(0, 0.05, len(ecq_cycle))
    
    # Define low-pass filter parameters
    cutoff_freq = 40.0  # Cutoff frequency in Hz
    order = 4  # Filter order
    
    # Create the low-pass filter (Butterworth filter)
    def lowpass_filter(data, cutoff, fs, order=4):
        nyquist = 0.5 * fs
        normal_cutoff = cutoff / nyquist
        b, a = butter(order, normal_cutoff, btype='low', analog=False)
        y = filtfilt(b, a, data)
        return y
    
    # Apply the low-pass filter to the noisy ECG cycle
    ecq_cycle_noisy_filtered = lowpass_filter(ecq_cycle_noisy, cutoff_freq, fs, order)
    
    # Compute correlation between the original and filtered ECG cycle
    correlation = np.corrcoef(ecq_cycle, ecq_cycle_noisy_filtered)[0, 1]
    st.info(f"Correlation between the original ECG cycle and the filtered ECG cycle: {correlation:.4f}")

    # Plot the ECG signals
    fig, ax = plt.subplots(3, 1, figsize=(12, 15))
    ax[0].plot(np.linspace(0, 1, len(ecq_cycle)), ecq_cycle, label='Original ECG Cycle', color='darkblue')
    ax[1].plot(np.linspace(0, 1, len(ecq_cycle_noisy)), ecq_cycle_noisy, label='Noisy ECG Cycle', color='red')
    ax[2].plot(np.linspace(0, 1, len(ecq_cycle_noisy_filtered)), ecq_cycle_noisy_filtered, label='Filtered ECG Cycle', color='forestgreen')
    
    for i, title in enumerate(["Original ECG Cycle", "Noisy ECG Cycle", "Filtered ECG Cycle"]):
        ax[i].set_title(title)
        ax[i].set_xlabel("Time (s)")
        ax[i].set_ylabel("Amplitude")
        ax[i].grid()
        ax[i].legend()
    
    st.pyplot(fig)
    


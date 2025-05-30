import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq
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

st.header("Type of Operation", divider="blue")
option = st.selectbox(
    "**Choose Type of Operation**",
    ("Operation on Signal", "Even & Odd Component", "Auto correlation", "Cross correlation"),
)

if option=="Operation on Signal":
    st.header("Parameters of Signal", divider="blue")
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
        


elif option=="Even & Odd Component":
    # Header for Even & Odd Component Analysis
    st.header("Even & Odd Component")

    # Introduction to even & odd decomposition
    st.markdown("""
                **Even & Odd Component Separation** facilitates the **separation of even and odd components** of a signal, allowing users to analyze fundamental signal properties. This is essential in **signal processing, Fourier analysis, and system characterization**.
                """)

    # Key Features Section
    st.header("Key Features")

    # Signal Type Selection
    st.subheader("- Signal Type Selection")
    st.markdown("""- Choose from **Sine, Cos, and Exponential signals**.""")
 
    # Even & Odd Component Decomposition Explanation
    st.subheader("- Even & Odd Component Decomposition")
    st.markdown(r"""
                A signal \( x(t) \) is decomposed into its even and odd components as follows:

                - **Even Component:**  
                $$ x_e(t) = \frac{x(t) + x(-t)}{2} $$
                
                - **Odd Component:**  
                $$ x_o(t) = \frac{x(t) - x(-t)}{2} $$
                """)
 
    # Graphical Representation
    st.subheader("- Graphical Representation")
    st.markdown("""
                - Visualize **original, even, and odd components** in the **time domain**.  
                - Analyze signal symmetry and properties through intuitive plots.  
                """)

    # Conclusion
    st.markdown("""
                This tool is ideal for **mathematical signal analysis, engineering applications, and educational purposes**, providing deep insights into signal behavior.
                """)

    st.header("", divider="blue")

    # Define time range
    t = np.linspace(-10, 10, 400)

    # Define signal functions
    def signal_sin(t):
        return np.sin(t)

    def signal_cos(t):
        return np.cos(t)

    # Dropdown to select the signal type
    signal_option = st.selectbox("Function:", ['Sine', 'Cosine', 'Signal 1'])

    # Function to return the selected signal
    def select_signal(signal_option):
        if signal_option == 'Sine':
            return signal_sin
        elif signal_option == 'Cosine':
            return signal_cos
        elif signal_option == 'Signal 1':
            t_custom = np.array([0, 1, 2, 3, 4, 5])
            x_custom = np.array([1, 1, 0, 1, 1, 2])
            return lambda t: np.interp(t, t_custom, x_custom, left=0, right=0)
        else:
            return lambda t: np.zeros_like(t)

    # Generate selected signal
    signal = select_signal(signal_option)
    x = signal(t)

    # Compute even and odd components
    even_signal = 0.5 * (x + np.flip(x))
    odd_signal = 0.5 * (x - np.flip(x))
    
    # Create a figure with 3 subplots
    fig, axes = plt.subplots(3, 1, figsize=(12, 15))
    ax1, ax2, ax3 = axes

    # Plot original signal
    ax1.plot(t, x, label='Original Signal', color='blue')
    ax2.plot(t, even_signal, label='Even Component', color='green')
    ax3.plot(t, odd_signal, label='Odd Component', color='red')

    # Display the plots on button click
    if st.button("Plot"):
        for ax, title in zip([ax1, ax2, ax3], ['Original Signal', 'Even Component', 'Odd Component']):
            ax.set_xlim(-10, 10)
            ax.set_ylim(-1.5, 2.5)
            ax.set_title(title)
            ax.set_xlabel('Time')
            ax.set_ylabel('Amplitude')
            ax.grid(True)
            ax.legend()
        # Show the figure in Streamlit
        st.pyplot(fig)

elif option=="Auto correlation":
    st.header("Autocorrelation & ESD", divider="blue")
    
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
    def generate_signal_2(signal_type, t):
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
        signal1 = generate_signal_2(signal_choice, t)
        noise = np.random.normal(0, 0.5, signal1.shape)
        signal2 = signal1 + noise

        auto_corr_signal1 = autocorrelation(signal1)
        auto_corr_signal2 = autocorrelation(signal2)
        lags = np.arange(-len(signal1) + 1, len(signal1))

        freqs, esd_noisy = calculate_esd(signal2, t)

        fig, axs = plt.subplots(4, 1, figsize=(10, 20))
        axs[0].plot(t, signal1, color='darkblue')
        axs[0].set_title(f'Original Signal ({signal_choice.capitalize()} Waveform)')
        axs[0].grid()
    
        axs[1].plot(t, signal2, color='red')
        axs[1].set_title('Original Signal + Noise')
        axs[1].grid()
    
        axs[2].plot(lags, auto_corr_signal1, label='Clean Signal', color='darkblue')
        axs[2].plot(lags, auto_corr_signal2, label='Noisy Signal', color='red')
        axs[2].set_title('Autocorrelation Results of Original Signal and Original+Noise')
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


elif option=="Cross correlation":
    st.header("Cross-Correlation", divider="blue")

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
    def generate_signal_3(signal_type, t):
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
        signal1 = generate_signal_3(signal_choice, t)
        noise = np.random.normal(0, 0.5, signal1.shape)
        signal2 = signal1 + noise
        corr_result = cross_correlation(signal1, signal2)
        lags = np.arange(-len(signal1) + 1, len(signal1))
    
        fig, axs = plt.subplots(3, 1, figsize=(13, 15))
    
        axs[0].plot(t, signal1, color='darkblue')
        axs[0].set_title(f'Original Signal ({signal_choice.capitalize()} Waveform)')
        axs[0].grid()
    
        axs[1].plot(t, signal2, color='red')
        axs[1].set_title('Original Signal + Noise')
        axs[1].grid()
    
        axs[2].plot(lags, corr_result, color='darkgreen')
        axs[2].set_title('Cross-Correlation Result of Original Signal and Original Signal + Noise')
        axs[2].set_xlabel('Lags')
        axs[2].set_ylabel('Cross-Correlation')
        axs[2].grid()
    
        st.pyplot(fig)

    


import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import base64 

# Configure Streamlit page settings
st.set_page_config(
    page_title="Signals & Systems Virtual Lab",
    layout="wide",
    page_icon=" "
)

# Function to encode image in Base64 for embedding
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Load and encode the logo image
logo_path = r"static/fcritlogo.png"
logo_base64 = get_base64_image(logo_path)

# HTML & CSS for header with logo
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
        display: flex;
        align-items: center;
        justify-content: space-between;
    }}
    .header h1 {{ margin-top: 48px; font-size: 30px; line-height: 2.5; }}
    .logo-container {{ position: absolute; top: 62px; right: 20px; }}
    .stApp {{ margin-top: 146px; padding-bottom: 80px; }}
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

# Footer section
st.markdown(
    """
    <div class="footer">
        <p>© 2025 Fr. Conceicao Rodrigues Institute of Technology. All rights reserved.</p>
    </div>
    """, 
    unsafe_allow_html=True
)

# Hide Streamlit menu and decorations
hide_menu= """
<style>
#MainMenu { visibility:hidden; }
</style>
"""
st.markdown(hide_menu, unsafe_allow_html=True)

st.markdown("""
<style>
	[data-testid="stDecoration"] { display: none; }
</style>""", unsafe_allow_html=True)

# Header for Even & Odd Component Analysis
st.header("Even & Odd Component", divider=True)

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

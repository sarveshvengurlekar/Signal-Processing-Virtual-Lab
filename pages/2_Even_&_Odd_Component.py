import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import base64 

# Set Streamlit page configuration
st.set_page_config(
    page_title="Signals Processing Virtual Lab",
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

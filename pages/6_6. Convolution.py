import streamlit as st 
import base64

# Set Streamlit page configuration
st.set_page_config(
    page_title="Signal Processing Virtual Lab",
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

st.header("Convolution", divider=True)

# Step 1
st.write("Step 1: Function f1(t) and Sliding f2(t)tau")
st.latex(r"(f_1 * f_2)(\tau) = \int_{-\infty}^{\infty} f_1(\tau) f_2(t - \tau) d\tau")
st.write("This step computes the overlap between f1(t) and the time-shifted version of f2(t).")

# Step 2
st.write("Step 2: Convolution  (f_1 * f_2)tau and Sliding f_3(t - tau).")
st.latex(r"((f_1 * f_2) * f_3)(\tau) = \int_{-\infty}^{\infty} (f_1 * f_2)(\tau) f_3(t - \tau) d\tau")
st.write("This step extends the operation by convolving the intermediate result with a new function f3(t).")

# Step 3
st.write("Step 3: Final Convolution (f1 * f2 * f3)(t)")
st.latex(r"(f_1 * f_2 * f_3)(t) = \int_{-\infty}^{\infty} ((f_1 * f_2)(\tau) f_3(t - \tau)) d\tau")
st.write("This results in a complete convolution of all three signals, producing the final output.")

# Conclusion
st.write("Conclusion: Convolution is a fundamental operation in signal processing, neural networks, and system analysis.")
st.write("It helps in understanding how multiple signals interact and combine in different systems.")

st.header("", divider="blue")

# Video options
video_options = {
    "Convolution (3 Rectangular Pulses)": r"Media/Convolution_3_pulses.mp4",
}

# Dropdown to select video
selected_video = st.selectbox("Select Convolution", list(video_options.keys()), index=0)

# Display selected video
st.video(video_options[selected_video])



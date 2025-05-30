import streamlit as st
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


st.header("Non-LTI System", divider=True)

st.markdown("""
A system is classified as **Linear Time-Invariant (LTI)** if it satisfies the principles of **superposition (linearity)** and **time invariance**. However, certain systems exhibit behaviors that violate these properties, making them **Non-LTI**.

## Non-Linearity & Time Variance
A system is **non-linear** if it does not satisfy **additivity and homogeneity**:

- **Additivity:** If an input \( x_1[n] \) produces output \( y_1[n] \) and \( x_2[n] \) produces \( y_2[n] \),
  If this fails, the system is **non-linear**.

- **Homogeneity (Scaling Property):** If an input \( ax[n] \) produces output \( ay[n] \), the system is **linear**. Otherwise, it is **non-linear**.

A system is **time-variant** if shifting the input by \( k \) samples does not result in an equivalent shift in the output.
""")

st.markdown("""
## Proving the Non-LTI Nature from the Given Graph

The provided figure contains three plots:

1. **Input Signal (Sine Wave) (Top Panel):** This represents the original input signal, which is a discrete sine wave.
2. **Output Signal (Delayed Input with 10 Samples) (Middle Panel):** The input is delayed by 10 samples.
3. **Output Signal (Delayed Output with 10 Samples) (Bottom Panel):** The output is delayed separately.

### Observations:
- If the system were **LTI**, delaying the input should result in a proportionally delayed output. However, from the graph, the delayed input does not generate the same delayed output.
- The **amplitude** of the delayed output differs from the amplitude of the delayed input, suggesting that the system violates the **scaling** property.
- Additionally, if the system were **time-invariant**, shifting the input by a given delay should shift the output by the same amount. However, the bottom plot shows an alteration in the output shape, confirming **time variance**.

## Conclusion
Since the system violates both **linearity** (due to changes in amplitude) and **time-invariance** (due to changes in the shape of the delayed response), it is classified as **Non-LTI**.
""")

st.header("",divider="blue")

# Ensure the image is responsive and does not exceed the viewable area
st.image(r"Media/Non_LTI_Th.jpg", use_container_width=True)

st.header("",divider="blue")

st.markdown("""
### Input : Sin Wave
""")

st.image(r"Media/Non_LTI_Sin.jpg", use_container_width=True)

st.header("",divider="blue")

st.markdown("""
### Input : Randn Wave
""")

st.image(r"Media/Non_LTI_Randn.png", use_container_width=True)

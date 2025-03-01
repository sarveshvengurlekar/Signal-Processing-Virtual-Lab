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
st.image(r"Media?Non_LTI.jpg", use_container_width=True)

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
    "Convolution (3 Rectangular Pulses)": r"C:\Users\sarve\Downloads\Coding\Python\DSP Internship\Streamlit\Signals & System Virtual Lab\Media\Convolution_3_pulses.mp4",
}

# Dropdown to select video
selected_video = st.selectbox("Select Convolution", list(video_options.keys()), index=0)

# Display selected video
st.video(video_options[selected_video])



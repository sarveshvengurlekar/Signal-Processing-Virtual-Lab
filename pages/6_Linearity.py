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

st.header("Linearity", divider=True)

st.markdown("""
## **Definition of Linearity**
A system is **linear** if it satisfies two conditions:

1. **Superposition Principle**:  
   If a system responds to input signals \\( x_1(t) \\) and \\( x_2(t) \\) as \\( y_1(t) \\) and \\( y_2(t) \\), then:
   \\[
   x(t) = a x_1(t) + b x_2(t) \Rightarrow y(t) = a y_1(t) + b y_2(t)
   \\]

2. **Scaling (Homogeneity)**:  
   If an input \\( x(t) \\) produces an output \\( y(t) \\), then scaling the input by \\( k \\) results in:
   \\[
   x'(t) = k x(t) \Rightarrow y'(t) = k y(t)
   \\]

If a system satisfies **both** conditions, it is considered **linear**.
""")

# Mathematical Proof
st.markdown("""
## **Mathematical Proof of Linearity**
The system response is analyzed using the **first and second derivatives** of \\( x_1(t) \\) and \\( x_2(t) \\).

#### **First Derivative:**
\\[
y'(t) = 2a x_1 + 2b x_2 + 3a + 3b
\\]

#### **Second Derivative:**
\\[
y''(t) = 2a x_1 + 2b x_2 + 3
\\]

If these equations follow the same **linear combination** as the input, the system is **linear**.
""")

# Section: Mathematical Proof
st.header("Mathematical Proof of Linearity in the Given Graphs")
st.markdown("""
The system's response is analyzed by computing the **first and second derivatives** of the input signals \\( x_1(t) \\) and \\( x_2(t) \\).  
The relationships are:

### **First Derivative:**
\\[
y'(t) = 2a \\cdot x_1 + 2b \\cdot x_2 + 3a + 3b
\\]

### **Second Derivative:**
\\[
y''(t) = 2a \\cdot x_1 + 2b \\cdot x_2 + 3
\\]

If the output equation follows the same **linear combination** as the input, the system is **linear**.
""")

# Section: Step-by-Step Explanation of Graphs
st.header("Step-by-Step Explanation of Graphs for Linearity Proof")

# Explanation of Graphs
st.subheader("- Top Left Graph: Input Signal \\( x_1(t) \\)")
st.markdown("""
- Represents one of the input signals \\( x_1(t) \\).
- The signal consists of discrete amplitude values plotted over time.
""")

st.subheader("- Top Right Graph: Input Signal \\( x_2(t) \\)")
st.markdown("""
- Represents the second input signal \\( x_2(t) \\).
- Similarly, the signal consists of discrete points sampled at different time indices.
""")

st.subheader("- Middle Left Graph: First Derivative \\( y'(t) \\)")
st.markdown(r"""
- Shows the **first derivative** of the combined input signals.
- Derived using the formula:

  \[
  y'(t) = 2a x_1 + 2b x_2 + 3a + 3b
  \]

- The **scaling and addition** of input signals maintain linearity.
""")

st.subheader("- Middle Right Graph: Second Derivative \\( y''(t) \\)")
st.markdown(r"""
- The second derivative is computed using:

  \[
  y''(t) = 2a x_1 + 2b x_2 + 3
  \]

- The transformation follows the original input structure, verifying **linearity**.
""")

st.subheader("- Bottom Graph: Comparison of \\( y'(t) \\) and \\( y''(t) \\)")
st.markdown("""
- The comparison of **first and second derivatives** ensures that the system follows the **principle of superposition**.
- The proportional relationship confirms that the system remains **linear**.
""")

# Section: Conclusion
st.header("Conclusion")
st.markdown("""
The graphs successfully prove that the system satisfies the **conditions of linearity**:

- **The sum of individual responses equals the response to the sum of inputs.**  
- **The first and second derivatives maintain a consistent transformation pattern.**  

Thus, the system is **verified to be Linear System.**.
""")

st.header("",divider="blue")

st.image(r"C:\Users\sarve\Downloads\Coding\Python\DSP Internship\Streamlit\Signals & System Virtual Lab\Media\Linearity.jpg")
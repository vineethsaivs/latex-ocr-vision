import streamlit as st
import ollama
from PIL import Image

# Page configuration
st.set_page_config(
    page_title="LaTeX OCR with Llama 3.2 Vision",
    page_icon="🦙",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Title and Description
st.title("🦙 LaTeX OCR with Llama 3.2 Vision")
st.markdown('<p style="margin-top: -15px;">Extract LaTeX code from images using Llama 3.2 Vision!</p>', unsafe_allow_html=True)
st.markdown("---")

# Sidebar Upload Section
with st.sidebar:
    st.header("Upload Image")
    uploaded_file = st.file_uploader("Choose an image...", type=['png', 'jpg', 'jpeg'])
    
    if uploaded_file is not None:
        # Display the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)
        
        if st.button("Extract LaTeX 🔍", type="primary"):
            with st.spinner("Processing image..."):
                try:
                    response = ollama.chat(
                        model='llama3.2-vision',
                        messages=[{
                            'role': 'user',
                            'content': """
                            Understand the mathematical equation in the provided image and output the corresponding LaTeX code.
                            Guidelines:
                            - Output ONLY the LaTeX code. No additional text or explanations.
                            - Do not add dollar signs ($) or documentclass.
                            - No simplifications or symbol explanations.
                            """,
                            'images': [uploaded_file.getvalue()]
                        }]
                    )
                    
                    # Handle response gracefully
                    st.session_state['ocr_result'] = response.get('message', {}).get('content', 'No LaTeX code detected.')
                except Exception as e:
                    st.error(f"⚠️ Error processing image: {str(e)}")

# Clear Button at the Top Right
col1, col2 = st.columns([6, 1])
with col2:
    if st.button("Clear 🗑️"):
        st.session_state.clear()
        st.rerun()

# Display OCR Results
if 'ocr_result' in st.session_state:
    st.markdown("### Extracted LaTeX Code")
    st.code(st.session_state['ocr_result'], language='latex')
    
    st.markdown("### Rendered LaTeX")
    cleaned_latex = st.session_state['ocr_result'].replace(r"\[", "").replace(r"\]", "")
    st.latex(cleaned_latex)
else:
    st.info("Upload an image and click 'Extract LaTeX' to see the results here.")

# Footer
st.markdown("---")
st.markdown('<p style="text-align: center;">Powered by Streamlit and Llama 3.2 Vision</p>', unsafe_allow_html=True)

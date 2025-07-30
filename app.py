import streamlit as st # type: ignore
import base64
from PIL import Image
import io
import requests

st.set_page_config(page_title="Image Analyser", layout="wide")
st.markdown("""
<style>
    .stApp {
        background-color:#0e1117;
        color:#fafafa
    }
    .stTextInput>div>div>input,.stTextArea>div>div>textarea {
        background-color:#1a1d23;
        border:1px solid #2d3748
    }
    .stButton>button {
        background:linear-gradient(135deg,#00d4ff 0%,#8b5cf6 100%);
        color:white;
        border:none;
        width:100%
    }
    .stFileUploader>div>div {
        background-color:#1a1d23;
        border:2px dashed #2d3748
    }
    #MainMenu,footer,header{visibility:hidden}
</style>
""", unsafe_allow_html=True)

def query_gemma(prompt, image=None):
    payload = {"model": "gemma3:4b", "prompt": prompt, "stream": False, "options": {"temperature": 0.1, "num_predict": 1000}}
    if image:
        buffered = io.BytesIO()
        image.save(buffered, format="PNG")
        payload["images"] = [base64.b64encode(buffered.getvalue()).decode()]
    try:
        response = requests.post("http://localhost:11434/api/generate", json=payload, timeout=300)
        return response.json()["response"] if response.status_code == 200 else f"Error: {response.status_code}"
    except Exception as e:
        return f"Error: {str(e)}"

st.markdown("<h1 style='text-align:center;color:#00d4ff'>Image Analyser</h1>", unsafe_allow_html=True)
col1, col2 = st.columns(2)

with col1:
    st.markdown("### Upload Image")
    uploaded_file = st.file_uploader("Choose an image file", type=['png', 'jpg', 'jpeg'])
    if uploaded_file and st.button("Preview Image"):
        st.image(Image.open(uploaded_file), use_container_width=True)

with col2:
    st.markdown("### Ask a Question")
    user_prompt = st.text_area("Enter your question:", height=76)

st.markdown("### Analysis")
if st.button("Analyze Image"):
    if uploaded_file and user_prompt:
        with st.spinner("Analyzing..."):
            response = query_gemma(user_prompt, Image.open(uploaded_file))
            st.markdown("**Response:**")
            st.markdown(response)
    else:
        st.warning("Please upload an image and enter a question")
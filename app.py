import streamlit as st
from dotenv import load_dotenv, find_dotenv
import os
import base64
from groq import Groq
from PIL import Image

load_dotenv(find_dotenv())

st.set_page_config(page_title="NutriScan AI", page_icon="🥗", layout="wide")

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    * { font-family: 'Inter', sans-serif; }

    .stApp { background-color: #f8fafc; }

    section[data-testid="stSidebar"] {
        background: #0f172a !important;
        border-right: 1px solid #1e293b;
    }
    section[data-testid="stSidebar"] * { color: #e2e8f0 !important; }
    section[data-testid="stSidebar"] h1 { color: #ffffff !important; font-size: 20px !important; }
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3 { color: #94a3b8 !important; font-size: 13px !important; text-transform: uppercase; letter-spacing: 1px; }
    section[data-testid="stSidebar"] p { color: #cbd5e1 !important; font-size: 14px !important; }
    section[data-testid="stSidebar"] hr { border-color: #1e293b !important; }

    .hero-section {
        background: linear-gradient(135deg, #0f172a 0%, #1e3a5f 50%, #0f172a 100%);
        border-radius: 20px;
        padding: 50px 40px;
        text-align: center;
        margin-bottom: 30px;
        border: 1px solid #1e293b;
    }
    .hero-badge {
        display: inline-block;
        background: rgba(16, 185, 129, 0.15);
        color: #10b981;
        border: 1px solid rgba(16, 185, 129, 0.3);
        border-radius: 50px;
        padding: 6px 16px;
        font-size: 13px;
        font-weight: 500;
        margin-bottom: 20px;
        letter-spacing: 0.5px;
    }
    .hero-title {
        font-size: 52px;
        font-weight: 700;
        color: #ffffff;
        margin: 0 0 15px 0;
        line-height: 1.1;
    }
    .hero-title span { color: #10b981; }
    .hero-subtitle {
        font-size: 18px;
        color: #94a3b8;
        margin: 0;
        font-weight: 400;
    }

    .upload-card {
        background: #ffffff;
        border-radius: 16px;
        padding: 30px;
        border: 2px dashed #e2e8f0;
        text-align: center;
        margin-bottom: 20px;
    }
    .upload-icon { font-size: 48px; margin-bottom: 15px; }
    .upload-title { font-size: 20px; font-weight: 600; color: #1e293b; margin-bottom: 8px; }
    .upload-sub { font-size: 14px; color: #94a3b8; }

    .stat-card {
        background: #ffffff;
        border-radius: 12px;
        padding: 20px;
        border: 1px solid #e2e8f0;
        text-align: center;
    }
    .stat-icon { font-size: 28px; margin-bottom: 8px; }
    .stat-label { font-size: 12px; color: #64748b; font-weight: 500; text-transform: uppercase; letter-spacing: 0.5px; }
    .stat-value { font-size: 15px; color: #0f172a; font-weight: 600; margin-top: 4px; }

    .stButton>button {
        background: linear-gradient(135deg, #10b981, #059669) !important;
        color: white !important;
        font-size: 16px !important;
        font-weight: 600 !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 16px 40px !important;
        width: 100% !important;
        letter-spacing: 0.3px;
    }
    .stButton>button:hover {
        box-shadow: 0 8px 25px rgba(16,185,129,0.35) !important;
    }

    .result-header {
        background: linear-gradient(135deg, #0f172a, #1e3a5f);
        border-radius: 16px 16px 0 0;
        padding: 20px 25px;
        display: flex;
        align-items: center;
        gap: 12px;
    }
    .result-header h3 {
        color: #ffffff !important;
        margin: 0;
        font-size: 18px;
        font-weight: 600;
    }
    .result-body {
        background: #ffffff;
        border-radius: 0 0 16px 16px;
        padding: 25px;
        border: 1px solid #e2e8f0;
        border-top: none;
        font-size: 15px;
        line-height: 1.8;
    }
    .result-body p, .result-body div { color: #1e293b !important; }

    .step-item {
        display: flex;
        align-items: center;
        gap: 12px;
        padding: 10px 0;
        border-bottom: 1px solid #1e293b;
    }
    .step-num {
        width: 28px;
        height: 28px;
        background: #10b981;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 13px;
        font-weight: 600;
        color: white;
        flex-shrink: 0;
    }

    h1, h2, h3 { color: #0f172a !important; }
    .stSuccess > div { border-radius: 12px !important; }
    .stWarning > div { border-radius: 12px !important; }
    </style>
""", unsafe_allow_html=True)

# ---- SIDEBAR ----
with st.sidebar:
    st.markdown("## 🥗 NutriScan AI")
    st.markdown("---")
    st.markdown("### UPLOAD IMAGE")
    uploaded_file = st.file_uploader("", type=["jpg", "jpeg", "png"])
    st.markdown("---")
    st.markdown("### HOW IT WORKS")
    st.markdown("""
    <div class="step-item">
        <div class="step-num">1</div>
        <span>Upload a food photo</span>
    </div>
    <div class="step-item">
        <div class="step-num">2</div>
        <span>Click Analyse this Food</span>
    </div>
    <div class="step-item">
        <div class="step-num">3</div>
        <span>Get full nutrition report</span>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("### SUPPORTED FORMATS")
    st.markdown("JPG &nbsp;•&nbsp; JPEG &nbsp;•&nbsp; PNG")
    st.markdown("Max file size: **200MB**")
    st.markdown("---")
    st.markdown("<p style='font-size:12px; color:#475569 !important;'>Powered by Groq AI + LLaMA 4</p>", unsafe_allow_html=True)

# ---- HERO ----
st.markdown("""
    <div class="hero-section">
        <div class="hero-badge">AI-Powered Nutrition Analysis</div>
        <h1 class="hero-title">Nutri<span>Scan</span> AI</h1>
        <p class="hero-subtitle">Upload any food image and get instant, detailed nutritional insights powered by advanced AI</p>
    </div>
""", unsafe_allow_html=True)

# ---- STATS ----
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown("""<div class="stat-card"><div class="stat-icon">⚡</div>
    <div class="stat-label">Analysis Speed</div><div class="stat-value">Under 5 seconds</div></div>""", unsafe_allow_html=True)
with col2:
    st.markdown("""<div class="stat-card"><div class="stat-icon">🎯</div>
    <div class="stat-label">Accuracy</div><div class="stat-value">AI-powered precision</div></div>""", unsafe_allow_html=True)
with col3:
    st.markdown("""<div class="stat-card"><div class="stat-icon">🥦</div>
    <div class="stat-label">Nutrients Tracked</div><div class="stat-value">Calories, Protein, Carbs, Fats</div></div>""", unsafe_allow_html=True)
with col4:
    st.markdown("""<div class="stat-card"><div class="stat-icon">📊</div>
    <div class="stat-label">Report Type</div><div class="stat-value">Full breakdown</div></div>""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ---- IMAGE PREVIEW ----
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Food Image", use_column_width=True)
    else:
        st.markdown("""
            <div class="upload-card">
                <div class="upload-icon">📸</div>
                <div class="upload-title">No Image Uploaded Yet</div>
                <div class="upload-sub">Upload a food photo from the left sidebar to get started</div>
            </div>
        """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ---- BUTTON ----
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    submit = st.button("🔍  Analyse this Food")

# ---- PROMPT ----
input_prompt = """
You are an expert nutritionist analyzing the food items in the image.
Start by determining if the image contains food items.
If the image does not contain any food items,
clearly state "No food items detected in the image."
and do not provide any calorie information.
If food items are detected,
start by naming the meal based on the image,
identify and list every ingredient you can find in the image,
and then estimate the total calories for each ingredient.
Summarize the total calories based on the identified ingredients.
Follow the format below:

If no food items are detected:
No food items detected in the image.

If food items are detected:
Meal Name: [Name of the meal]

1. Ingredient 1 - estimated calories
2. Ingredient 2 - estimated calories
----
Total estimated calories: X

Finally, mention whether the food is healthy or not,
and provide the percentage split of protein, carbs, and fats in the food item.
Also, mention the total fiber content in the food item and any other important details.

Note: Always identify ingredients and provide an estimated calorie count,
even if some details are uncertain.
"""

# ---- FUNCTIONS ----
def get_groq_response(input_prompt, image):
    image_data = base64.b64encode(image[0]["data"]).decode("utf-8")
    mime_type = image[0]["mime_type"]
    response = client.chat.completions.create(
        model="meta-llama/llama-4-scout-17b-16e-instruct",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "image_url", "image_url": {"url": f"data:{mime_type};base64,{image_data}"}},
                    {"type": "text", "text": input_prompt}
                ]
            }
        ],
        max_tokens=1024
    )
    return response.choices[0].message.content

def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        return [{"mime_type": uploaded_file.type, "data": bytes_data}]
    else:
        raise FileNotFoundError("No image uploaded")

# ---- RESULT ----
if submit:
    if uploaded_file is None:
        st.warning("⚠️ Please upload a food image first from the left sidebar!")
    else:
        with st.spinner("Analysing your food with AI... Please wait!"):
            image_data = input_image_setup(uploaded_file)
            response = get_groq_response(input_prompt, image_data)
        st.success("✅ Analysis Complete!")
        st.markdown("<br>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([0.5, 3, 0.5])
        with col2:
            st.markdown("""
                <div class="result-header">
                    <span style="font-size:24px;">🍽️</span>
                    <h3 style="color:#ffffff !important; margin:0; font-size:18px; font-weight:600;">Nutrition Analysis Report</h3>
                </div>
            """, unsafe_allow_html=True)
            st.markdown(f"""
                <div class="result-body">
                    <p style="color:#1e293b !important;">{response.replace(chr(10), '<br>')}</p>
                </div>
            """, unsafe_allow_html=True)
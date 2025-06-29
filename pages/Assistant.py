import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()

# 🔐 Load API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# 📌 Initialize Gemini Flash model
model = genai.GenerativeModel("gemini-1.5-flash")

# 🧠 Base Prompt Template
BASE_PROMPT = """
You are an AI medico-legal assistant trained on Indian medical law and ethics.

Given the scenario below, identify:
1. Legal issue(s)
2. Doctor’s legal and ethical duties
3. Relevant documentation/forms
4. Legal risk involved

Respond professionally, clearly, and concisely.

Scenario: "{}"
"""

# 🖼️ Streamlit Config
st.set_page_config(page_title="ClinGuard AI", page_icon="⚖️", layout="wide")
st.markdown("<style>footer {visibility: hidden;}</style>", unsafe_allow_html=True)

# 📌 Sidebar
with st.sidebar:
    st.title("🩺 ClinGuard AI")
    st.markdown("Your medico-legal assistant.")
    st.markdown("""
        **Use cases:**  
        - Emergency refusals  
        - Consent & minors  
        - Medico-legal forms  
        - Death reporting
    """)
    st.markdown("Built with ❤️ using Gemini & Streamlit")

# 🧠 Main App
st.title("⚖️ ClinGuard AI – Medico-Legal Assistant")
st.markdown("##### Get quick, context-aware legal guidance for Indian healthcare scenarios.")
st.markdown("Fill in a clinical situation or choose a type from the dropdown to get started.")

# 🔽 Optional Scenario Template
col1, col2 = st.columns([2, 3])
with col1:
    case_type = st.selectbox("Choose a sample case type (optional):", [
        "— Select —",
        "Refusal of Treatment",
        "Emergency without Consent",
        "Minor Seeking Procedure",
        "Police Brought Patient",
        "Death under Unnatural Circumstances"
    ])
    prefill = {
        "Refusal of Treatment": "A patient with a head injury is conscious but refuses treatment.",
        "Emergency without Consent": "An unconscious accident victim is brought to ER without relatives.",
        "Minor Seeking Procedure": "A 13-year-old requests abortion without informing her parents.",
        "Police Brought Patient": "A young woman is brought by police with injuries. No family present.",
        "Death under Unnatural Circumstances": "A patient dies during treatment for poisoning. Relatives suspect foul play."
    }
else_case = prefill.get(case_type, "")
    
with col2:
    scenario = st.text_area("📝 Describe the clinical situation:", value=else_case)

# 🚀 Generate Button
if st.button("📋 Get Legal Guidance") and scenario.strip():
    with st.spinner("Analyzing scenario with Gemini Flash..."):
        prompt = BASE_PROMPT.format(scenario.strip())
        try:
            response = model.generate_content(prompt)
            st.success("✅ Here's your medico-legal insight:")
            formatted_response = response.text.replace("\n", "<br>")
            st.markdown(
                f"<div style='padding: 1rem; background-color: #f9f9f9; border-radius: 8px; border: 1px solid #ddd;'>{formatted_response}</div>",
                unsafe_allow_html=True
            )

        except Exception as e:
            st.error(f"❌ Something went wrong: {e}")

# 💡 Extra Help
with st.expander("💡 How to write a good scenario prompt"):
    st.markdown("""
    - Keep it short but specific  
    - Mention patient’s condition and situation clearly  
    - Examples:  
      - *'Unconscious 20-year-old male brought to ER after road accident. No attendants present.'*  
      - *'Minor female requests treatment for assault. Parents unaware.'*
    """)

# 📎 Footer
st.markdown("---")
st.caption("🚨 This tool provides AI-generated suggestions only. Not a substitute for formal legal advice.")

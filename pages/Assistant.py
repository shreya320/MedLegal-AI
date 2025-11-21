import streamlit as st
import sys
sys.path.append(".")

from components.faiss import get_relevant_chunks, get_similar_cases
from components.gemini import get_gemini_response
from components.prompts import build_main_prompt, build_followup_prompt
from components.followup import render_extras


# ─── UI Config ─────────────────────────────────────
st.set_page_config(page_title="MedLegal AI", page_icon="⚖️", layout="wide")
st.markdown("<style>footer {visibility: hidden;}</style>", unsafe_allow_html=True)

# ─── Sidebar ───────────────────────────────────────
with st.sidebar:
    st.title("🩺 MedLegal AI")
    st.markdown("Your medico-legal assistant.")
    st.markdown("""
        **Use cases:**  
        - Emergency refusals  
        - Consent & minors  
        - Medico-legal forms  
        - Death reporting
    """)

# ─── Page Title ─────────────────────────────────────
st.title("⚖️ MedLegal AI – Medico-Legal Assistant")
st.markdown("##### Get quick, context-aware legal guidance for Indian healthcare scenarios.")

# ─── Input Section ─────────────────────────────────
col1, col2 = st.columns([2, 3])
with col1:
    case_type = st.selectbox("Choose a sample case type (optional):", [
        "— Select —", "Refusal of Treatment", "Emergency without Consent",
        "Minor Seeking Procedure", "Police Brought Patient", "Death under Unnatural Circumstances"
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

# ─── Generate Button ───────────────────────────────
if st.button("📋 Get Legal Guidance") and scenario.strip():
    with st.spinner("Retrieving legal documents..."):
        try:
            context = get_relevant_chunks(scenario)
            final_prompt = build_main_prompt(context, scenario)
            answer = get_gemini_response(final_prompt)

            st.session_state["guidance_answer"] = answer
            st.session_state["guidance_context"] = context
            st.session_state["guidance_scenario"] = scenario

        except Exception as e:
            st.error(f"❌ Gemini failed: {e}")

# ✅ Display stored response
if "guidance_answer" in st.session_state:
    answer = st.session_state["guidance_answer"]
    context = st.session_state["guidance_context"]

    st.success("✅ Here's your grounded medico-legal insight:")
    st.markdown(answer)

    with st.expander("📄 Show retrieved legal context"):
        st.markdown(context)

    render_extras(st.session_state["guidance_scenario"], answer)

# ─── Prompt Tips ───────────────────────────────────
with st.expander("💡 How to write a good scenario prompt"):
    st.markdown("""
    - Keep it short but specific  
    - Mention patient’s condition and setting  
    - Examples:  
      - *Unconscious 20-year-old male brought to ER after road accident. No attendants present.*  
      - *Minor female requests treatment for assault. Parents unaware.*
    """)

st.markdown("---")
st.caption("🚨 This tool provides AI-generated suggestions only. Not a substitute for formal legal advice.")

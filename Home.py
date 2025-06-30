import streamlit as st

st.set_page_config(page_title="MedLegal AI", page_icon="⚖️", layout="centered")

st.title("⚖️ MedLegal AI")
st.subheader("AI-Powered Medico-Legal Assistant for Indian Doctors")

st.markdown("""
Welcome to **MedLegal AI**, the tool to help Indian healthcare professionals assess legal duties, obligations, and documentation in complex scenarios.

---

**Use cases:**  
- Emergency treatment without consent  
- Refusal of care  
- Handling minors  
- Deaths under suspicious circumstances  
- Medico‑legal case documentation  
""")

# ✅ Button that links to another page
st.page_link("pages\Assistant.py", label="🧠 Start Assistant", icon="📝")


st.markdown("---")
st.caption("📌 Not a substitute for formal legal advice.")

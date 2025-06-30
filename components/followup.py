import streamlit as st
from components.prompts import build_followup_prompt, build_doc_prompt
from components.gemini import get_gemini_response
from components.faiss import get_similar_cases


def render_extras(scenario, answer):
    st.markdown("---")

    # Follow-up Q
    follow_up = st.text_input("💬 Ask a follow-up question:", key="followup_q")
    if follow_up:
        followup_prompt = build_followup_prompt(scenario, answer, follow_up)
        followup_answer = get_gemini_response(followup_prompt)
        st.markdown("### 🧠 Follow-up Answer:")
        st.markdown(followup_answer)

    # Documentation suggestions
    if st.button("📋 What should I document in this case?", key="doc_btn"):
        doc_prompt = build_doc_prompt(scenario)
        doc_answer = get_gemini_response(doc_prompt)
        st.markdown("### 📋 Suggested Documentation:")
        st.markdown(doc_answer)

    # Similar cases
    if st.button("👀 Show Similar Cases from Legal Corpus", key="similar_btn"):
        similar_cases = get_similar_cases(scenario)
        st.markdown("### 👥 Similar Cases:")
        for i, doc in enumerate(similar_cases, 1):
            st.markdown(f"**{i}.** {doc.page_content[:400]}...")

    if "doc_answer" not in st.session_state:
        st.session_state.doc_answer = None


# ⚖️ MedLegal AI – An Indian Medico-Legal Assistant for Doctors

MedLegal AI is an AI-powered assistant built to help Indian doctors make informed, ethical, and legally sound decisions in challenging clinical situations. It provides instant, context-aware medico-legal guidance grounded in Indian medical law and ethics.

## 🚀 Features

- 🔍 **Scenario-based Legal Guidance**: Enter clinical scenarios (e.g. refusal of treatment, unconscious patients, minors seeking procedures) and receive legally grounded advice.
- 🧠 **RAG-powered Retrieval**: Combines LLMs (Gemini 1.5 Flash) with legal documents using Retrieval-Augmented Generation (RAG) for accurate, verifiable answers.
- 📋 **Documentation Suggestions**: Know exactly what to record for legal safety.
- 💬 **Follow-up Q&A**: Ask clarifying legal questions within context.
- 📄 **Relevant Case Retrieval**: View similar legal cases/documents from the database.
- ⚠️ **Risk Assessment**: Instantly see if the case has high/medium/low legal risk.
- 🇮🇳 Built with **Indian medical law** in mind — including MCI/NMC guidelines, IPC sections, and forms like MLC/Annexure D.

## 🧰 Tech Stack

- `Python` + `Streamlit` for the interactive UI
- `Gemini 1.5 Flash` (Google Generative AI) for LLM-powered responses
- `LangChain` + `FAISS` for document retrieval
- `HuggingFace Embeddings` with `MiniLM` for vector similarity
- `.env` file for secure API key handling

📚 Sources
Indian Medical Council Regulations (MCI/NMC)

Indian Penal Code (IPC) Sections

Legal guidelines from AIIMS, WHO, MOHFW, and medico-legal repositories

Documents retrieved via FAISS-based vector search

🧑‍⚕️ Example Use Cases
A patient with a head injury refuses treatment

A 13-year-old girl seeks an abortion without telling her parents

A patient dies under suspicious circumstances during treatment

An unconscious victim is brought by police for evaluation

⚠️ Disclaimer
This tool provides AI-generated guidance based on publicly available medico-legal documents. It is not a substitute for legal counsel, and should be used for informational purposes only. Consult a qualified legal advisor for case-specific recommendations.


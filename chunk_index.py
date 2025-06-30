import os
import pickle
from pathlib import Path
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.document_loaders import PyPDFLoader

# ─────── Paths ─────────────────────────────────────────────────
DOCS_DIR = "legal_docs"
ARTIFACTS_DIR = "artifacts"
os.makedirs(ARTIFACTS_DIR, exist_ok=True)

# ─────── Step 1: Load and Chunk PDFs ───────────────────────────
def load_and_chunk_documents():
    all_chunks = []

    for filename in os.listdir(DOCS_DIR):
        if filename.endswith(".pdf"):
            file_path = os.path.join(DOCS_DIR, filename)
            print(f"📄 Loading: {filename}")
            loader = PyPDFLoader(file_path)
            pages = loader.load_and_split()

            # Optional: Add source metadata
            for page in pages:
                page.metadata["source"] = filename

            all_chunks.extend(pages)

    # Split into 300-word chunks with 50-word overlap
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    split_docs = splitter.split_documents(all_chunks)
    print(f"✅ Total Chunks: {len(split_docs)}")
    return split_docs

# ─────── Step 2: Create Embeddings ─────────────────────────────
def embed_documents(chunks):
    print("🔍 Loading embedding model...")
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    
    print("📦 Building FAISS index...")
    vectorstore = FAISS.from_documents(chunks, embeddings)

    # Save index
    vectorstore.save_local(f"{ARTIFACTS_DIR}/index")
    print("✅ FAISS index saved to /artifacts/index")

    # Save original chunks too
    with open(f"{ARTIFACTS_DIR}/chunks.pkl", "wb") as f:
        pickle.dump(chunks, f)
    print("✅ Chunk data saved to /artifacts/chunks.pkl")

# ─────── MAIN ──────────────────────────────────────────────────
if __name__ == "__main__":
    docs = load_and_chunk_documents()
    embed_documents(docs)

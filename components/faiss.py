from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2",
    model_kwargs={"device": "cpu"}
)

# Load FAISS DB
db = FAISS.load_local("artifacts/index", embedding, allow_dangerous_deserialization=True)

def get_relevant_chunks(query, k=4):
    results = db.similarity_search(query, k=k)
    return "\n\n".join([doc.page_content for doc in results])

def get_similar_cases(query, k=3):
    return db.similarity_search(query, k=k)

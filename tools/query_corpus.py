import os
import argparse
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

# Configuration
PERSIST_DIR = "corpus_index"
EMBEDDING_MODEL = "all-MiniLM-L6-v2"
TOP_K = 5

def query_index(query: str):
    if not os.path.exists(PERSIST_DIR):
        print(f"Error: Vector store directory '{PERSIST_DIR}' not found.")
        print("Please run 'python tools/build_index.py' first.")
        return

    print(f"Initializing embedding model '{EMBEDDING_MODEL}'...")
    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)

    print(f"Loading vector store from '{PERSIST_DIR}'...")
    vectorstore = Chroma(
        persist_directory=PERSIST_DIR, 
        embedding_function=embeddings
    )

    print(f"\nSearching for: '{query}'\n")
    results = vectorstore.similarity_search_with_score(query, k=TOP_K)

    if not results:
        print("No matching results found.")
        return

    for i, (doc, score) in enumerate(results):
        source = os.path.basename(doc.metadata.get('source', 'Unknown source'))
        page = doc.metadata.get('page', 'Unknown page')
        
        # Lower distance/score is usually better in Chroma
        print(f"--- Result {i+1} (Distance: {score:.4f}) ---")
        print(f"Source: {source} (Page {page})")
        print(f"Content:\n{doc.page_content.strip()}\n")
        print("-" * 60 + "\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Query the PDF corpus RAG index.")
    parser.add_argument("query", type=str, help="The specific concept, spell, or character to search for.")
    args = parser.parse_args()
    
    query_index(args.query)

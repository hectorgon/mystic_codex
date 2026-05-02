import os
import argparse
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

# Configuration
PERSIST_DIR = "corpus_index"
SCRATCH_DIR = "scratch"
EMBEDDING_MODEL = "all-MiniLM-L6-v2"
TOP_K = 15

def extract_spells(query: str):
    if not os.path.exists(PERSIST_DIR):
        print(f"Error: Vector store directory '{PERSIST_DIR}' not found.")
        print("Please run 'python tools/build_index.py' first.")
        return

    if not os.path.exists(SCRATCH_DIR):
        os.makedirs(SCRATCH_DIR)

    print(f"Initializing embedding model '{EMBEDDING_MODEL}'...")
    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)

    print(f"Loading vector store from '{PERSIST_DIR}'...")
    vectorstore = Chroma(
        persist_directory=PERSIST_DIR, 
        embedding_function=embeddings
    )

    print(f"\nExtracting top {TOP_K} chunks for: '{query}'\n")
    results = vectorstore.similarity_search_with_score(query, k=TOP_K)

    if not results:
        print("No matching results found.")
        return

    # Clean query string for filename
    safe_query = "".join([c if c.isalnum() else "_" for c in query])
    output_file = os.path.join(SCRATCH_DIR, f"raw_spell_extract_{safe_query}.md")

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f"# Raw Extraction for: {query}\n\n")
        f.write("This file contains raw text chunks from the vector database. ")
        f.write("Use these chunks to synthesize a final spell/practice document.\n\n")
        
        for i, (doc, score) in enumerate(results):
            source = os.path.basename(doc.metadata.get('source', 'Unknown source'))
            page = doc.metadata.get('page', 'Unknown page')
            
            f.write(f"## Result {i+1} (Distance: {score:.4f})\n")
            f.write(f"**Source:** {source} (Page {page})\n\n")
            f.write(f"```text\n{doc.page_content.strip()}\n```\n\n")
            f.write("---\n\n")

    print(f"Extraction complete! Wrote raw chunks to '{output_file}'")
    print("You can now review this file to synthesize the final lore document.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract raw text chunks for spells/practices into a scratch file.")
    parser.add_argument("query", type=str, help="The specific spell or practice to extract (e.g., 'protection spell').")
    args = parser.parse_args()
    
    extract_spells(args.query)

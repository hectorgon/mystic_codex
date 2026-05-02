import os
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

# Configuration
CORPUS_DIR = "corpus"
PERSIST_DIR = "corpus_index"
EMBEDDING_MODEL = "all-MiniLM-L6-v2"
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200

def build_index():
    print(f"Loading PDFs from '{CORPUS_DIR}'...")
    if not os.path.exists(CORPUS_DIR):
        os.makedirs(CORPUS_DIR)
        print(f"Created '{CORPUS_DIR}' directory. Please add PDF files to it.")
        return

    loader = PyPDFDirectoryLoader(CORPUS_DIR)
    documents = loader.load()
    
    if not documents:
        print(f"No PDF documents found in '{CORPUS_DIR}'. Please add some PDFs.")
        return

    print(f"Loaded {len(documents)} document pages.")
    
    print("Splitting texts into chunks...")
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        length_function=len,
    )
    chunks = text_splitter.split_documents(documents)
    print(f"Split into {len(chunks)} text chunks.")

    print(f"Initializing embedding model '{EMBEDDING_MODEL}'...")
    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)

    print(f"Building and persisting Chroma vector store to '{PERSIST_DIR}'...")
    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=PERSIST_DIR
    )
    print("Vector database built successfully.")

if __name__ == "__main__":
    build_index()

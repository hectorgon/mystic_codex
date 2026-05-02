# Skill: Index Corpus (RAG System)

This skill dictates how the agent should index, query, and extract lore from the large esoteric PDF corpora within the `corpus/` directory. Due to the massive size of these documents, we do not read them line-by-line into context. Instead, we rely on a Retrieval-Augmented Generation (RAG) system utilizing free, local, open-source embedding models.

## Pre-requisite Tools

To perform these tasks, the agent utilizes a suite of Python scripts in the `tools/` directory. If these scripts do not exist or need modification, the agent should follow the guidelines below to create/modify them.

1. **`tools/build_index.py`**: A script to chunk the PDFs and build the vector database.
2. **`tools/query_corpus.py`**: A script to query the vector database and retrieve relevant context.

### Technology Stack Constraints
- **Document Loading & Chunking**: Use `Langchain` and `PyPDFDirectoryLoader` with `RecursiveCharacterTextSplitter`.
- **Embeddings**: strictly use free and open-source models via `SentenceTransformers` (e.g., `all-MiniLM-L6-v2`) via HuggingFace embeddings. Do NOT use paid APIs like OpenAI for embeddings.
- **Vector Store**: Use `ChromaDB` configured to persist locally in a `corpus_index/` directory at the project root.

## Agent Instructions: Building the Index

When requested to update or build the index for the PDFs:

1. Ensure `tools/build_index.py` exists and is properly configured with the stack constraints above.
2. Run the script from the `mystic_codex` environment:
   ```bash
   python tools/build_index.py
   ```
3. Verify that the `corpus_index/` directory was successfully populated with ChromaDB files.

## Agent Instructions: Querying the Corpus

When requested to assist in populating the `lore/` directory using information from the corpus:

1. Identify the specific esoteric concept, character, or spell to research (e.g., "Mojo bag creation", "Crossroads ritual").
2. Ensure `tools/query_corpus.py` is available. It should accept a search query as an argument and return the top matching text chunks from the vector store.
3. Run the query script:
   ```bash
   python tools/query_corpus.py "Your specific query here"
   ```
4. Analyze the returned chunks from the terminal output. 
5. Use this synthesized information to write or update the appropriate markdown files in the `lore/` directory following the project's persona and lore-writing style. 
6. Ensure that any extracted lore is properly categorized into characters, spells, locations, or concepts.

## Modifying the Pre-built Tools

If the user requests adjustments to the indexing strategy (e.g., changing chunk size or overlap) or search mechanism (e.g., returning more results `top_k`):
- Open and edit `tools/build_index.py` or `tools/query_corpus.py`.
- Adhere strictly to the open-source and local constraints.
- Re-run `tools/build_index.py` if the chunking or embedding strategy was modified, to rebuild the database from scratch.

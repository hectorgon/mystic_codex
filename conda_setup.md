# Conda Environment Setup

This project uses `conda` to manage dependencies, ensuring seamless installation of data science and NLP libraries required for corpus analysis.

## Prerequisites
- [Miniconda](https://docs.conda.io/en/latest/miniconda.html) or [Anaconda](https://www.anaconda.com/) installed on your system.

## Creating the Environment

1. Open your Anaconda Prompt or terminal.
2. Create a new environment named `mystic_codex` with Python 3.11 (recommended):
   ```bash
   conda create -n mystic_codex python=3.11 -y
   ```
3. Activate the environment:
   ```bash
   conda activate mystic_codex
   ```

## Installing Dependencies

Once activated, you can install the required packages. As the project evolves, we'll maintain a `requirements.txt` or `environment.yml`. For now, you can install some baseline tools for PDF analysis:

```bash
# Example baseline packages and RAG tools
conda install -c conda-forge PyPDF2 pdfplumber pandas jupyter pypdf langchain langchain-community chromadb sentence-transformers -y
```

When you are done working, you can deactivate the environment:
```bash
conda deactivate
```

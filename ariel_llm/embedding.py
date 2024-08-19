"""Embedding functions"""
from langchain_ollama import OllamaEmbeddings


# TODO: make this a factory class
def get_embedding_function(size: str = "large") -> OllamaEmbeddings:
    """Get the embedding function which is nomic-embed-text or mxbai-embed-large"""
    model_name = "nomic-embed-text" if size == "small" else "mxbai-embed-large"
    return OllamaEmbeddings(model=model_name)

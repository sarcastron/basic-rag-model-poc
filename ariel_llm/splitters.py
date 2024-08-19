"""Splitters used to split text into smaller units."""
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.schema.document import Document


def split_documents(
    docs: list[Document], chunk_size: int = 1000, chunk_overlap: int = 0
):
    """Split a list of documents into smaller chunks."""
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len,
        is_separator_regex=False,
    )
    return text_splitter.split_documents(docs)


def calculate_chunk_ids(chunks: list[Document]):
    """Calculate IDs for each chunk."""
    for i, chunk in enumerate(chunks):
        chunk.metadata["id"] = f"{chunk.metadata['source']}-ch-{i}"
    return chunks

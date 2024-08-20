"""Repo for interacting with the ChromaDB."""

import os
import shutil
from langchain_chroma import Chroma
from langchain.schema.document import Document
from rich import print as r_print
from ariel_llm.embedding import get_embedding_function  # noqa
from ariel_llm.splitters import calculate_chunk_ids  # noqa

# TODO: Make this configurable
CHROMA_PATH = "chromadb"


def add_to_chroma(chunks: list[Document]):
    """Add documents to ChromaDB."""
    # Load the existing database.
    db = Chroma(
        persist_directory=CHROMA_PATH, embedding_function=get_embedding_function()
    )

    # Calculate Page IDs.
    chunks_with_ids = calculate_chunk_ids(chunks)

    # Add or Update the documents.
    existing_items = db.get(include=[])  # IDs are always included by default
    existing_ids = set(existing_items["ids"])
    r_print(f"Number of existing documents in DB: {len(existing_ids)}")

    # Only add documents that don't exist in the DB.
    new_chunks = []
    for chunk in chunks_with_ids:
        if chunk.metadata["id"] not in existing_ids:
            new_chunks.append(chunk)

    if len(new_chunks) > 0:
        r_print(f"👉 Adding new documents: {len(new_chunks)}")
        new_chunk_ids = [chunk.metadata["id"] for chunk in new_chunks]
        db.add_documents(new_chunks, ids=new_chunk_ids)
    else:
        r_print("✅ No new documents to add")


def clear_database():
    """Clear the ChromaDB data store."""
    if os.path.exists(CHROMA_PATH):
        shutil.rmtree(CHROMA_PATH)

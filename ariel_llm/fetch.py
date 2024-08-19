"""Crawl URLs and extract text from it. Then split it and generate embeddings. Save embeddings to ChromaDB"""

import os
from rich import print as r_print
from ariel_llm.bs_transformer import beautiful_soup_transformer
from ariel_llm.splitters import split_documents
from ariel_llm.chromadb_repo import add_to_chroma


def fetch_data(urls: list[str]):
    """
    Given a list of URLs, fetch the text from the URLs and insert into ChromaDB.
    This performs the following steps:
    1. Fetch the text from the URLs.
    2. Split the text into smaller chunks.
    3. Generate embeddings for each chunk.
    4. Save the embeddings to ChromaDB.
    """
    os.environ["USER_AGENT"] = "Ariel-llm 0.0.1"
    r_print("Crawling URLs and extracting text from it...")
    docs_transformed = beautiful_soup_transformer(urls)

    r_print(f"Splitting {len(docs_transformed)} documents...")
    chunks = split_documents(docs_transformed, chunk_size=800, chunk_overlap=80)
    r_print(f"Number of documents after splitting: {len(chunks)}")

    add_to_chroma(chunks)

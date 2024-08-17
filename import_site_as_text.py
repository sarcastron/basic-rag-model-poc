"""Crawl URLs and extract text from it. Then split it and generate embeddings. Save embeddings to ChromaDB"""

import os
from rich import print as r_print
from ariel_llm.bs_transformer import beautiful_soup_transformer
from ariel_llm.splitters import split_documents
from ariel_llm.chromadb_repo import add_to_chroma

os.environ["USER_AGENT"] = "Ariel-llm 0.0.1"
urls = [
    "https://learn.prospero.ai/net-options-sentiment",
    "https://learn.prospero.ai/net-social-sentiment",
    "https://learn.prospero.ai/net-institutional-flow",
    "https://learn.prospero.ai/short-pressure-rating",
    "https://learn.prospero.ai/dark-pool-rating",
]

r_print("Crawling URLs and extracting text from it...")
docs_transformed = beautiful_soup_transformer(urls)

r_print(f"Splitting {len(docs_transformed)} documents...")
chunks = split_documents(docs_transformed, chunk_size=800, chunk_overlap=80)
r_print(f"Number of documents after splitting: {len(chunks)}")

add_to_chroma(chunks)

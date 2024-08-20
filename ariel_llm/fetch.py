"""Crawl URLs and extract text from it. Then split it and generate embeddings. Save embeddings to ChromaDB"""

import os
from rich import print as r_print
from langchain_community.document_loaders.sitemap import SitemapLoader
from ariel_llm.bs_transformer import beautiful_soup_transformer
from ariel_llm.splitters import split_documents
from ariel_llm.chromadb_repo import add_to_chroma


def fetch_urls(urls: list[str], user_agent: str = "Ariel-llm 0.0.1"):
    """
    Given a list of URLs, fetch the text from the URLs and insert into ChromaDB.
    This performs the following steps:
    1. Fetch the text from the URLs.
    2. Split the text into smaller chunks.
    3. Generate embeddings for each chunk.
    4. Save the embeddings to ChromaDB.

    Args:
        urls (list[str]): List of URLs to fetch data from.
        user_agent (str, optional): User agent to use for fetching the URLs. Defaults to "Ariel-llm 0.0.1".
    """
    os.environ["USER_AGENT"] = user_agent
    r_print("Crawling URLs and extracting text...")
    docs_transformed = beautiful_soup_transformer(urls)

    r_print(f"Splitting {len(docs_transformed)} documents...")
    chunks = split_documents(docs_transformed, chunk_size=800, chunk_overlap=80)
    r_print(f"Number of documents after splitting: {len(chunks)}")

    add_to_chroma(chunks)


def fetch_using_sitemap_xml(
    sitemap_url: str, filter_urls: list[str] = None, user_agent: str = "Ariel-llm 0.0.1"
):
    """
    Fetch data from the URLs in a sites sitemap.xml file.
    https://python.langchain.com/v0.2/docs/integrations/document_loaders/sitemap/

    Args:
        sitemap_url (str): URL of the sitemap.xml file.
        filter_urls (list[str], optional): List of URLs to filter. Defaults to None. Can be a list of string literals or regex patterns.
        user_agent (str, optional): User agent to use for fetching the URLs. Defaults to "Ariel-llm 0.0.1".
    """
    os.environ["USER_AGENT"] = user_agent
    sitemap_loader = SitemapLoader(web_path=sitemap_url, filter_urls=filter_urls)
    docs = sitemap_loader.load()
    r_print(f"Splitting {len(docs)} documents...")
    chunks = split_documents(docs, chunk_size=800, chunk_overlap=80)
    r_print(f"Number of documents after splitting: {len(chunks)}")

    add_to_chroma(chunks)

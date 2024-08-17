"""Crawl a website and extract text from it."""

from typing import List
from langchain_community.document_loaders import AsyncChromiumLoader
from langchain_community.document_transformers import BeautifulSoupTransformer
from langchain.schema.document import Document


def beautiful_soup_transformer(urls: list[str]) -> List[Document]:
    """Extract text from a website using BeautifulSoup."""
    loader = AsyncChromiumLoader(urls)
    html_docs = loader.load()

    # Transform
    bs_transformer = BeautifulSoupTransformer()
    return bs_transformer.transform_documents(html_docs)

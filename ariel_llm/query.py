"""Query the RAG model with a given query text."""

from langchain_chroma import Chroma
from langchain.prompts import ChatPromptTemplate
from langchain_community.llms.ollama import Ollama
from rich import print as r_print, inspect
from ariel_llm.chromadb_repo import CHROMA_PATH
from ariel_llm.embedding import get_embedding_function

MODEL = "llama3:instruct"

PROMPT_TEMPLATE = """
Answer the question based only on the following context:

{context}

---

Answer the question based on the above context: {question}.
"""


def query_rag(query_text: str):
    """Query the RAG model."""
    embedding_function = get_embedding_function()
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)

    # Search the DB.
    results = db.similarity_search_with_score(query_text, k=5)

    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)

    prompt = prompt_template.format(context=context_text, question=query_text)
    inspect(context_text)

    model = Ollama(model=MODEL)
    response_text = model.invoke(prompt)

    sources = [doc.metadata.get("id", None) for doc, _score in results]
    r_print("\n\n[bold green]Answer: [/bold green]")
    r_print(response_text)
    r_print("\n\n[bold cyan]Sources: [/bold cyan]")
    for source in sources:
        r_print(f"[#575757]{source}[/#575757]")
    return response_text

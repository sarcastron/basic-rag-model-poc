# pylint: disable=wrong-import-position,import-outside-toplevel
"""Entrypoint for the CLI."""
import os
from typing import Optional, List
import typer
from typing_extensions import Annotated
from rich import print as r_print

# Set the default user agent for fetching URLs. This can be overridden by the user.
os.environ["USER_AGENT"] = "Ariel-llm 0.0.1"

app = typer.Typer()
fetch_app = typer.Typer()
app.add_typer(fetch_app, name="fetch", help="Fetch data from URLs or sitemap.xml file")


@app.command("clear")
def clear():
    """Clear the ChromaDB data store."""
    from ariel_llm.chromadb_repo import clear_database
    clear_database()


@app.command("query")
def query(question: Annotated[str, typer.Option("-q")] = None):
    """Query the LLM. If a question is not provided, user will be prompted to enter a question."""
    from ariel_llm.query import query_rag, MODEL
    r_print(f"Using model: [bold #FFA500]{MODEL}[/bold #FFA500]")
    if question is not None:
        query_rag(question)
        raise typer.Exit()
    r_print("[yellow]Entering interactive mode. Type [/yellow][magenta]`/bye`[/magenta] [yellow]to exit.[/yellow]")
    while True:
        question = typer.prompt("Ask a question")
        if question == "/bye":
            break
        query_rag(question)
        print("\n\n")
    r_print("Okay, bye-bye! 👋")


@fetch_app.command("urls")
def fetch(urls: List[str]):
    """Fetch data from a list of URLs provided as arguments."""
    from ariel_llm.fetch import fetch_urls
    fetch_urls(urls)


@fetch_app.command("sitemap")
def fetch_sitemap(sitemap_url: str, filter_urls: Optional[List[str]] = None):
    """Fetch data from the URLs in a sitemap.xml file."""
    from ariel_llm.fetch import fetch_using_sitemap_xml
    fetch_using_sitemap_xml(sitemap_url, filter_urls)


if __name__ == "__main__":
    app()

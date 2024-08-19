"""Entrypoint for the CLI."""
from typing import Optional
import typer
from typing_extensions import Annotated
from ariel_llm.query import query_rag
from ariel_llm.fetch import fetch_data


def main(subcommand: str, args: Annotated[Optional[str], typer.Argument()] = None):
    """Create CLI."""
    if subcommand in ["ask", "query"]:
        query_text = args[0]
        query_rag(query_text)
    elif subcommand == "fetch":
        urls = [
            "https://learn.prospero.ai/how-ratings-work",
            "https://learn.prospero.ai/net-options-sentiment",
            "https://learn.prospero.ai/net-social-sentiment",
            "https://learn.prospero.ai/net-institutional-flow",
            "https://learn.prospero.ai/short-pressure-rating",
            "https://learn.prospero.ai/dark-pool-rating",
            "https://learn.prospero.ai/profitability",
            "https://learn.prospero.ai/growth",
            "https://learn.prospero.ai/downside-breakout",
            "https://learn.prospero.ai/upside-breakout",
            "https://learn.prospero.ai/market-similarity",
            "https://learn.prospero.ai/long-term-signals",
            "https://learn.prospero.ai/short-term-signals",
            "https://learn.prospero.ai/how-ratings-work",
        ]
        fetch_data(urls)
    else:
        raise ValueError(f"Unknown subcommand: {subcommand}")


if __name__ == "__main__":
    typer.run(main)

# ScrapeGraph: https://scrapegraph-ai.readthedocs.io/en/latest/scrapers/graphs.html

# ? Currently supports single page scrapes. Look @ docs for multi-page scrapes.
# ? Prompt can make it return multiple outputs. Right now we're returning top 5 key words + summary

import os
from dotenv import load_dotenv
from scrapegraphai.graphs import OmniScraperGraph


def keywords_summary(url: str):
    load_dotenv()
    openai_key = os.getenv('OPENAI_API_KEY')

    PROMPT = "Extract the top 5 topic content keywords and a 750 word summary based on a synthesis of the content of this webpage (including text and images)."

    graph_config = {
        "llm": {
            "api_key": openai_key,
            "model": "gpt-4o"
        },
    }

    # Create smartgraph instance
    # ? can possibly also impose schema for output
    smart_scraper_graph = OmniScraperGraph(
        prompt=PROMPT,
        source=url,
        config=graph_config
    )

    result = smart_scraper_graph.run()

    return list(result.values())

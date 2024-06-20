# ScrapeGraph: https://scrapegraph-ai.readthedocs.io/en/latest/scrapers/graphs.html

# ? Currently supports single page scrapes. Look @ docs for multi-page scrapes.

import os
from dotenv import load_dotenv
from scrapegraphai.graphs import SmartScraperGraph


def get_topic_keywords(url: str) -> list[str]:
    load_dotenv()
    openai_key = os.getenv('OPENAI_API_KEY')

    PROMPT = "Extract the top 5 topic content keywords based on a summary and synthesis of the content of this webpage."

    graph_config = {
        "llm": {
            "api_key": openai_key,
            "model": "gpt-4o"
        },
    }

    # Create smartgraph instance
    smart_scraper_graph = SmartScraperGraph(
        prompt=PROMPT,
        source=url,
        config=graph_config
    )

    result = smart_scraper_graph.run()

    keywords = list(result.values())[0]

    return keywords

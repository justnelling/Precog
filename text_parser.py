# ScrapeGraph: https://scrapegraph-ai.readthedocs.io/en/latest/scrapers/graphs.html

# ? Currently supports single page scrapes. Look @ docs for multi-page scrapes.

import os
from dotenv import load_dotenv

from scrapegraphai.graphs import SmartScraperGraph

load_dotenv()

openai_key = os.getenv('OPENAI_API_KEY')

URL = 'https://www.daviddeutsch.org.uk/blog/'
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
    source=URL,
    config=graph_config
)

result = smart_scraper_graph.run()
print(result)

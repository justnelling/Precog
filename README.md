# Action points

23/6/2024

1. Flesh out browser extension to include button to save AI synthesis to web app
2. Start building main web app page:  
   a. Endpoint to receive data from server (not from browser extension)
   b. A landing page where user can access all these saved summaries
   c. Knowledge graph visualisation
3. Come back to VideoParser -- feels clunky right now (having to download the video transcript and then analyse that. Need to research better way of executing this)
4. Once we can get the keywords categorisations for both text and video, figure out how we want to organise it into a central store. The key here is that we want it modular so its like a file-based bookmark system.

---

# Core

This app aims to be a central, universal bookmarker and knowledge-resource organizer. It will be able to intuitively and cohesively see what media you're currently consuming and:

1. Intelligently parse out its topic keywords
2. From these keywords parse out the relevant categories it might fall under
3. Retrieve from a saved profile of your bookmark categories, and suggest where this fits in those categories.
4. If allowed, perform automated actions on your behalf to store this media content in that category
5. Summarise its content and add it as a note to this categorisation folder

## Current scope

1. Focus on text + video media forms
2. Figure out how to have this automatically integrated into your browsing experience
3. Integrate with app experience (not just web browsers)

## Stretch goal

1. Create a knowledge graph mapping of how your category folders relate to each other.
2. Suggest top 5 recent media / research interests
3. Scrape the web and suggests new sources where to look for new information

## Questions

1. Should this be a web app / browser extension / OS-integrated orchestration thing (like Apple intelligence?)

## Orientation

1. Before we go deep into the intelligent content categorisation and parsing, we should perhaps first focus on the simple intelligent indexing / bookmarking of content for you first. That's really the main draw of the app.
2. Then second stage is to focus on the intelligent categorisation of the content, the relations via knowledge graph, etc.

### Resources

#### Text

1. use scrapegraph to improve URL text / image parsing (https://scrapegraph-ai.readthedocs.io/en/latest/scrapers/graphs.html)

#### Video

1. use The Pipe for video analysis? (https://thepi.pe/) --> paid API but this might be the fastest
2. Building from scratch with llamaindex going to be so laborious --> https://www.llamaindex.ai/blog/multimodal-rag-for-advanced-video-processing-with-llamaindex-lancedb-33be4804822e

Eliminated:

1. Microsoft Azure AI Video Indexer (doesn't work for youtube urls)
2. AssemblyAI (doesn't work for youtube urls)'

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

### Action points

1. text_parser (takes in URL) (DONE)
2. Implemented video_transcriber
3. Once we can get the keywords categorisations for both text and video, figure out how we want to organise it into a central store. The key here is that we want it modular so its like a file-based bookmark system.
4. Then we want to be able to visualise the relationships between different folders and see how they might relate to each other / how the most recent media relates to each other

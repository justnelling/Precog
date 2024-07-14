import asyncio
import re
from urllib.parse import urlparse, parse_qs
from youtube_transcript_api import YouTubeTranscriptApi
from openai import AsyncOpenAI
import instructor
from pydantic import BaseModel, Field, conlist

# ? YouTube videos only


class Summary_Keywords(BaseModel):
    summary: str = Field(...,
                         description="A concise and insightful 200-500 word summary of the video content")
    keywords: conlist(str, min_length=1, max_length=5) = Field(...,
                                                               description="Top 5 most salient keywords or phrases from the video")


def extract_video_id(url):
    # Patterns for YouTube URLs
    patterns = [
        r'^https?:\/\/(?:www\.)?youtube\.com\/watch\?v=([^&]+)',
        r'^https?:\/\/(?:www\.)?youtube\.com\/embed\/([^?]+)',
        r'^https?:\/\/(?:www\.)?youtube\.com\/v\/([^?]+)',
        r'^https?:\/\/youtu\.be\/([^?]+)',
        r'^https?:\/\/(?:www\.)?youtube\.com\/shorts\/([^?]+)'
    ]

    # Try to match the URL with each pattern
    for pattern in patterns:
        match = re.match(pattern, url)
        if match:
            return match.group(1)

    # If no pattern matches, try parsing the URL
    parsed_url = urlparse(url)
    if parsed_url.netloc in ['youtube.com', 'www.youtube.com']:
        query_params = parse_qs(parsed_url.query)
        if 'v' in query_params:
            return query_params['v'][0]

    # If we still haven't found an ID, raise an exception
    raise ValueError(f"Could not extract video ID from URL: {url}")


async def get_youtube_transcript(video_id):
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    return " ".join([entry['text'] for entry in transcript])


async def summarize_video(client, transcript):
    # # If the transcript is very long, we'll need to truncate it
    # max_tokens = 4000  # Adjust based on your needs and model limits
    # truncated_transcript = transcript[:max_tokens]

    response = await client.chat.completions.create(
        model="gpt-3.5-turbo-16k",  # Using a model with larger context
        response_model=Summary_Keywords,
        messages=[
            {"role": "system",
             "content": "You are an AI assistant that summarizes video transcripts and extracts key topics. Provide a concise and insightful 200-500 word summary and exactly 5 keywords or short phrases that best represent the main topics of the video."
             },
            {"role": "user",
             "content": f"Here's a video transcript. Please summarize it in 200-500 words and provide a list of 5 keywords:\n\n{
                 transcript}"
             }
        ]
    )
    return response


async def process_video(youtube_url):
    video_id = extract_video_id(youtube_url)
    transcript = await get_youtube_transcript(video_id)

    client = instructor.from_openai(AsyncOpenAI())
    result = await summarize_video(client, transcript)

    return result.summary, result.keywords


async def main(youtube_url):
    summary, keywords = await process_video(youtube_url)
    print(summary)
    print(keywords)

if __name__ == "__main__":
    asyncio.run(main("https://www.youtube.com/watch?v=QMW4AqbuSGg"))

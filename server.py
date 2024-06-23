from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict, List

# text-parser
from text_parser import keywords_summary

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# create storage for keywords
ks_store: Dict[str, List[str]] = {}


def process_url(url: str):
    scrape_results = keywords_summary(url)
    ks_store[url] = scrape_results


@app.post('/submit-url')
async def submit_url(url: str, background_tasks: BackgroundTasks):
    print(f'Received URL: {url}')

    background_tasks.add_task(process_url, url)

    return {"message": "Keywords generation starting..."}


@app.get('/keywords')
async def get_keywords(url: str):
    print("-" * 40)
    print(f"Getting keywords for {url}")

    if url in ks_store:
        return {"keywords": ks_store[url][0], "summary": ks_store[url][1]}
    else:
        raise HTTPException(
            status_code=404, detail="Keywords not found for provided URL")

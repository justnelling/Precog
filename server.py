from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# text-parser
from text_parser import get_topic_keywords

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


class Item(BaseModel):
    url: str

#! Need to come back and read about asnycio event order and how to call other async events in a loop: https://stackoverflow.com/questions/76142431/how-to-run-another-application-within-the-same-running-event-loop


def process_url(url: str):
    keywords = get_topic_keywords(url)

    print("Keywords: ", keywords)


@app.post('/submit-url')
async def submit_url(item: Item, background_tasks: BackgroundTasks):
    print(f'Received URL: {item.url}')

    background_tasks.add_task(process_url, item.url)

    return {"message": "Process started"}

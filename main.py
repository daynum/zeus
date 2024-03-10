from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

import logging
import uvicorn
from ytdl import download_video
from google_news import get_news_by_topic

# Set up logging
logging.basicConfig(filename='ytdl.log', level=logging.DEBUG)

app = FastAPI()

@app.get("/ytdl/")
def download_yt_video(video_url: str, extract_audio:bool, download_path:str):
    logging.debug(f'Downloading Video URL: {video_url}')
    print("Extract Audio is: ", extract_audio)
    filename = download_video(video_url, download_path=download_path, extract_audio=extract_audio)
    return JSONResponse(content={"filename": filename})

@app.get("/jsonfix/")
def fix_json(json_blob: str):
    # TODO: Implement JSON fixer
    pass

@app.get("/hacker_news/")
def get_hacker_news():
    pass

@app.get("/news/")
def get_news(topic: str):
    return get_news_by_topic(topic)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=3000, reload=True)
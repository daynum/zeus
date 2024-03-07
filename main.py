import yt_dlp as yt
from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import os
import subprocess
import logging
import uvicorn

# Set up logging
logging.basicConfig(filename='translator.log', level=logging.DEBUG)

def download_video(video_url: str, download_path:str=os.getcwd()) -> str:
    video_id = video_url.split("/watch?v=")[-1]
    YTDL_OPTS = {
        'outtmpl': f'{download_path}{video_id}.%(ext)s',
    }

    youtube = yt.YoutubeDL(YTDL_OPTS)
    video_info = youtube.sanitize_info(youtube.extract_info(video_url, download=False))

    video_ext = video_info['ext']

    video_title = video_info['title']
    valid_chars = ' -_.()abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    limited_title = ''.join(c for c in video_title if c in valid_chars)[:30]
    

    video_filename = f"{download_path}{video_id}.{video_ext}"
    new_filename = f'{download_path}{limited_title}-[{video_id}].{video_ext}'
    logging.debug(f'Starting video download for {download_path}{video_filename}')
    youtube.download(video_url)
    logging.debug('Video download completed')

    os.rename(video_filename, new_filename)

    return new_filename

def extract_audio(video_filename: str) -> str:
    audio_filename = video_filename.split('.')[0] + '.ogg'
    logging.debug('Starting audio extraction')
    extract_audio_ffmpeg_command = f'ffmpeg -i {video_filename} -vn -acodec libvorbis {audio_filename}.ogg'
    proc = subprocess.Popen('pwsh.exe', stdin=subprocess.PIPE, stdout=subprocess.PIPE, encoding='utf8')
    stdout, stderr = proc.communicate(extract_audio_ffmpeg_command)
    logging.debug('Audio extraction completed')

    return audio_filename

app = FastAPI()

@app.get("/ytdl/")
def read_root(video_url: str, download_path:str):
    logging.debug(f'Downloading Video URL: {video_url}')
    filename = download_video(video_url, download_path=download_path)
    return JSONResponse(content={"filename": filename})
    # return JSONResponse()     {"filename": filename}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=3000, reload=True)
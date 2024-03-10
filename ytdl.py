import yt_dlp as yt
import os
import subprocess
import logging

# Set up logging
logging.basicConfig(filename='ytdl.log', level=logging.DEBUG)

def download_video(video_url: str, extract_audio: bool, download_path:str=os.getcwd()+"/") -> str:
    logging.debug('Starting video download')
    logging.debug('video_url: ' + video_url)
    logging.debug('download_path: ' + download_path)

    video_id = video_url.split("/watch?v=")[-1]
    logging.debug('video_id: ' + video_id)
    YTDL_OPTS = {
        'outtmpl': f'{download_path}{video_id}.%(ext)s',
    }

    youtube = yt.YoutubeDL(YTDL_OPTS)
    raw_video_info = youtube.extract_info(video_url, download=False)
    logging.debug('Raw video info: ' + str(raw_video_info))
    video_info = youtube.sanitize_info(youtube.extract_info(video_url, download=False))
    logging.debug('Video info: ' + str(video_info))
    video_ext = video_info['ext']

    video_title = video_info['title']
    valid_chars = ' -_.()abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    limited_title = ''.join(c for c in video_title if c in valid_chars)[:30]
    

    video_filename = f"{download_path}{video_id}.{video_ext}"
    new_filename = f'{download_path}{limited_title}-[{video_id}].{video_ext}'
    logging.debug(f'Starting video download for {video_filename}')
    youtube.download(video_url)
    logging.debug('Video download completed')

    os.rename(video_filename, new_filename)

    if(extract_audio):
        logging.debug('Extracting audio from video: {new_filename}')
        print(f'Extracting audio from video: {new_filename}')
        audio_filename = extract_audio_from_videofile(new_filename)
    return new_filename

def extract_audio_from_videofile(video_filename: str) -> str:
    audio_filename = video_filename.split('.')[0] + '.ogg'
    logging.debug('Starting audio extraction')
    extract_audio_ffmpeg_command = f'ffmpeg -i "{video_filename}" -vn -acodec libvorbis "{audio_filename}.ogg"'
    logging.debug(f'Running command: {extract_audio_ffmpeg_command}')
    proc = subprocess.Popen('pwsh.exe', stdin=subprocess.PIPE, stdout=subprocess.PIPE, encoding='utf8')
    stdout, stderr = proc.communicate(extract_audio_ffmpeg_command)
    logging.debug('Audio extraction completed')

    return audio_filename

if __name__ == '__main__':
    video_url = 'https://www.youtube.com/watch?v=2Vv-BfVoq4g'
    video_filename = download_video(video_url)
    # audio_filename = extract_audio(video_filename)
    # print(f'Audio file: {audio_filename}')
    print(f'Video file: {video_filename}')
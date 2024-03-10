## ZEUS
Hobby project for utilitties I use, made into a local website.

1. YT-DL (/ytdl/)
2. Google News RSS display (/news/)

NOTE:
Frontend is written in [Svelte](https://github.com/sveltejs) and runs on Nodejs runtime.
Backend is python and uses python 3.12.1

### Usage
1. First install the packages from `requirementt.txt` eiotehr in a virtual environment or your local python installation.
2. Install the node packages by doing `npm install` in the project directory.
3. Run the node server with `npm run dev -- --open --host` and python backed with `python main.py`

You can use 2 terminals, or split terminal to run the backend and frontend processes.
Or, you can use this command for windows to run them both `npm run dev -- --open --host & python main.py`
# Phase 02: Build MVP (10 minutes)

## Goal

Create the smallest working version of the app: download one video using `yt-dlp`.

## Steps

1. Create a new file called `main.py`.
2. Add the simple download code below.
3. Run the script and examine the output.

```python
from pathlib import Path
import yt_dlp

Path("videos").mkdir(exist_ok=True)

url = "https://www.youtube.com/watch?v=jNQXAC9IVRw"

# Save inside videos/ using the video title as the filename
ydl_options = {
    "outtmpl": "videos/%(title)s.%(ext)s"
}

with yt_dlp.YoutubeDL(ydl_options) as ydl:
    ydl.download([url])
```

## Checkpoint

Run:

```bash
python main.py
```

Confirm that:

- The script runs without an error.
- A video file appears in the `videos` folder.

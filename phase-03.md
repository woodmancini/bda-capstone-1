# Phase 03: Refactor to improve (10 minutes)

## Goal

Improve the code structure by moving the download logic out of `main.py` and into a reusable function in `library.py`.

## Steps

1. Delete the video file from the `videos/` folder if it already exists.
2. Create a new file called `library.py`.
3. Inside `library.py`, create a function called `download_video`.
4. Move the `yt-dlp` download logic from `main.py` into that function.
5. Update `main.py` so it imports and calls the function.

## Function shape

```python
def download_video(url):
    # download one video
    ...
```

## Update `main.py`

Your `main.py` should call the function from `library.py`.

Make sure `main.py` uses the standard `__main__` check:

```python
from ...

if __name__ == "__main__":
    ...
```

## Checkpoint

Run:

```bash
python main.py
```

The app should still download the same video, but the download logic should now live in `library.py`.

After running the script, a fresh video file should appear in the `videos/` folder.

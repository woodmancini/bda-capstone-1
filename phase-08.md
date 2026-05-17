# Phase 08: Add video metadata (lab extension)

## Goal

Use `yt-dlp` to collect metadata for each video and create a richer dataset.

The final dataset should include:

```python
{
    "title": "...",
    "duration": 10,
    "uploader": "...",
    "view_count": 12345,
    "ext": "mp4",
    "url": "..."
}
```

## Steps

1. Create a new function in `library.py` for extracting video metadata.
2. Call this function when each individual download is triggered.
3. Store the metadata in a list of dictionaries.
4. After all downloads finish, create a new CSV file from that data structure.
5. Save the new dataset in the `data/` folder.

## Metadata pattern

Use this code pattern to test metadata extraction for one video:

```python
import yt_dlp

urls = [
    "https://www.youtube.com/watch?v=jNQXAC9IVRw",
]

ydl_options = {
    "quiet": True,
    "skip_download": True,
}

with yt_dlp.YoutubeDL(ydl_options) as ydl:
    for url in urls:
        info = ydl.extract_info(url, download=False)

        print("Title:", info.get("title"))
        print("Duration:", info.get("duration"))
        print("Uploader:", info.get("uploader"))
        print("Views:", info.get("view_count"))
        print("Extension:", info.get("ext"))
        print("URL:", url)
```

## Recreate this as a function

The metadata logic should live in `library.py`, not directly in `main.py`.

Suggested function name:

```python
get_video_metadata(url)
```

The function should return a dictionary like this:

```python
{
    "title": info.get("title"),
    "duration": info.get("duration"),
    "uploader": info.get("uploader"),
    "view_count": info.get("view_count"),
    "ext": info.get("ext"),
    "url": url,
}
```

## Create a new dataset

It is better to collect all metadata first, then create a new file after everything finishes.

For example:

```python
metadata_rows = []

for url in urls:
    metadata = get_video_metadata(url)
    metadata_rows.append(metadata)

# create the new CSV after the loop finishes
```

You can use `csv.DictWriter` to write the new dataset:

```python
import csv

with open("data/video_metadata.csv", "w", newline="") as file:
    fieldnames = ["title", "duration", "uploader", "view_count", "ext", "url"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(metadata_rows)
```

Suggested output filename:

```text
data/video_metadata.csv
```

## Checkpoint

Run:

```bash
python main.py
```

Confirm that:

- The metadata extraction function lives in `library.py`.
- The function is called when each individual download is triggered.
- The app creates `data/video_metadata.csv`.
- The new CSV contains `title`, `duration`, `uploader`, `view_count`, `ext`, and `url`.

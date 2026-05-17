# Phase 09: Make the downloader safer (lab extension)

## Goal

Improve the downloader so one failed video does not stop the whole program.

In real data projects, downloads can fail because:

- a URL is broken
- the network is slow
- YouTube blocks or delays a request
- the video is unavailable
- the request takes too long

Your app should handle these problems and keep going.

## Steps

1. Add simple error handling to the download function in `library.py`.
2. Add a timeout to the `yt-dlp` options.
3. Return a result dictionary for each download.
4. Record whether each download succeeded or failed.
5. Update the Markdown report with any failed URLs.

## Add safer `yt-dlp` options

You can add a socket timeout to the `yt-dlp` options:

```python
ydl_options = {
    "outtmpl": "videos/%(title)s.%(ext)s",
    "socket_timeout": 30,
}
```

This means `yt-dlp` should not wait forever if the connection is too slow.

## Use `try` and `except`

Wrap the download code so the program can recover from an error:

```python
def download_video(url):
    ydl_options = {
        "outtmpl": "videos/%(title)s.%(ext)s",
        "socket_timeout": 30,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_options) as ydl:
            ydl.download([url])

        return {
            "url": url,
            "status": "success",
            "error": "",
        }

    except Exception as error:
        return {
            "url": url,
            "status": "failed",
            "error": str(error),
        }
```

## Keep downloading after an error

When you download multiple videos, store each result:

```python
results = []

for url in urls:
    result = download_video(url)
    results.append(result)
```

Then print or report the failed downloads:

```python
for result in results:
    if result["status"] == "failed":
        print("Failed:", result["url"])
        print("Error:", result["error"])
```

## Update the report

Add a new section to `reports/sequential_report.md`:

```md
## Download status

Successful downloads:
Failed downloads:
```

If any videos failed, include the URL and the error message.

## Checkpoint

Run:

```bash
python main.py
```

Confirm that:

- The app does not crash if one video fails.
- The app keeps trying the remaining videos.
- Each download returns a success or failed status.
- Failed URLs are printed in the terminal or added to the report.
- The report includes a download status section.

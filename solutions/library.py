from pathlib import Path
import yt_dlp
import csv

def download_video(url):

    Path("videos").mkdir(exist_ok=True)

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

def read_video_urls(csv_path):

    result = []

    with open(csv_path, newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            result.append(row["url"])

    return result

def get_video_metadata(url):

    ydl_options = {
        "quiet": True,
        "skip_download": True,
    }

    result = {}

    with yt_dlp.YoutubeDL(ydl_options) as ydl:

        info = ydl.extract_info(url, download=False)

        result["Title:"] = info.get("title")
        result["Duration:"] = info.get("duration")
        result["Uploader:"] = info.get("uploader")
        result["Views:"] = info.get("view_count")
        result["Extension:"] = info.get("ext")
        result["URL:"] = url
    
    return result
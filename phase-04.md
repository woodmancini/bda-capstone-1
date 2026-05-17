# Phase 04: Read the data (10 minutes)

## Goal

Add a function to `library.py` that reads video URLs from a CSV file.

## Data file

The CSV file is located at:

```text
data/video_urls.csv
```

It contains 5 starter video URLs with titles.

Columns:

| title                      | url                                         |
| -------------------------- | ------------------------------------------- |
| Me at the zoo              | https://www.youtube.com/watch?v=jNQXAC9IVRw |
| 10 sec 2D Test animation   | https://www.youtube.com/watch?v=BB49x_uMlGA |
| [TEST] 10 Second Countdown | https://www.youtube.com/watch?v=Hm5ieMoxc4c |
| My Snowboarding Skillz     | https://www.youtube.com/watch?v=LeAltgu_pbM |
| 10 Second Timer            | https://www.youtube.com/watch?v=tCDvOQI3pco |

## Steps

1. In `library.py`, create a function that reads the CSV file.
2. Use Python's built-in `csv` module.
3. Return the URLs from the `url` column.
4. Import the CSV-reading function into `main.py`.
5. Print the list of URLs to check that it works.

## Recreate this as a function

Suggested function name `read_video_urls(csv_path)`.

```python
import csv

with open("data/video_urls.csv", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row["title"], row["url"])
```

The CSV reader should live in `library.py`, not directly in `main.py`.

## Import it in `main.py`

Your `main.py` should import the CSV-reading function from `library.py`. **Print the list of URLs to check that it works.**

## Checkpoint

Run:

```bash
python main.py
```

Confirm that:

- The app reads from `data/video_urls.csv`.
- The app prints a Python list of video URLs.
- The CSV-reading code lives in `library.py`.

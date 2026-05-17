# Phase 05: Download in serial (10 minutes)

## Goal

Use the CSV reader from Phase 04 to download all videos one by one and save a simple Markdown report.

## Steps

1. Import the CSV-reading function from `library.py`.
2. Read the URLs from `data/video_urls.csv`.
3. Download each video one by one.
4. Measure the time for each download.
5. Measure the total execution time.
6. Create a simple Markdown report file manually inside the `reports/` folder.
7. Add a short time and space complexity note to the Markdown report.

## Use the CSV reader

Your `main.py` should use the function you created in Phase 04:

```python
import ...

if __name__ == "__main__":
    ...
```

## Measure time

Use `time.perf_counter()`:

```python
import time

start = time.perf_counter()

# code to time goes here

end = time.perf_counter()
elapsed = end - start
```

Use `round()` to show the time with 2 decimal points:

```python
serial_time = round(elapsed, 2)
print(f"Serial execution: {serial_time}")
```

Your terminal output should look like this:

```text
Serial execution: XX.XX
```

## Create a simple Markdown report

First, manually create a new Markdown file inside the `reports/` folder.

Suggested filename:

```text
reports/sequential_report.md
```

Add this starter content to the file:

```md
# Report

## Serial execution

Total time:
```

After the file exists, update your Python code so it writes the real serial execution time into this Markdown file.

Also update the report with a short answer to this question:

```text
What is the time complexity and space complexity of downloading the videos one by one?
```

Add your answer below the serial execution time:

```md
## Complexity

Time complexity:
Space complexity:
```

## Checkpoint

Run:

```bash
python main.py
```

Confirm that:

- The app reads URLs using the function from `library.py`.
- Videos download one by one. Check the `videos/` folder.
- A report appears in `reports/sequential_report.md`.
- The report includes a short time and space complexity note.
- The terminal prints `Serial execution: XX.XX` with the time rounded to 2 decimal points.

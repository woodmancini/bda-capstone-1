# Phase 06: Parallelize and compare (10 minutes)

## Goal

Use `multiprocessing.Pool` to download the same videos in parallel, then compare serial and parallel performance.

## Steps

1. Keep the serial version from Phase 05.
2. In `main.py`, comment out the serial download execution so it does not run again.
3. Add a parallel version using `multiprocessing.Pool`.
4. Download the same videos in parallel.
5. Measure the total parallel execution time.
6. Add the parallel result below the serial result in the same Markdown report.
7. Compare serial vs parallel performance.

## Comment out serial execution

Do not run the serial downloads again in this phase.

In `main.py`, comment out the part that runs the serial download loop. Keep the code in the file, but prevent it from executing while you test the parallel version.

## Parallel pattern

```python
from multiprocessing import Pool

with Pool() as pool:
    results = pool.map(download_video, urls)
```

## Measure parallel time

Use `round()` to show the time with 2 decimal points:

```python
parallel_time = round(elapsed, 2)
print(f"Parallel execution: {parallel_time}")
```

Your terminal output should look like this:

```text
Parallel execution: XX.XX
```

## Update the report

Use the same report file from Phase 05:

```text
reports/sequential_report.md
```

Add the parallel result below the serial result:

```md
# Report

## Serial execution

Total time: XX.XX seconds

## Parallel execution

Total time: YY.YY seconds

## Comparison

Speed improvement: XX%
```

Use the serial time from Phase 05 when calculating the speed improvement. Do not overwrite the serial section.

You do not need to add a complexity comment in this phase. The complexity question belongs to the serial version from Phase 05.

## Checkpoint

Confirm that:

- The app updates `reports/sequential_report.md`.
- The Markdown report contains a serial execution section.
- The Markdown report contains a parallel execution section below the serial section.
- The Markdown report contains a comparison section.
- The terminal prints `Parallel execution: XX.XX` with the time rounded to 2 decimal points.

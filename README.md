# BDA capstone 1: parallel video downloader

This repository is a starter project for an in-class coding activity. Students will build a small Python app that downloads YouTube videos, records timing information, and compares serial processing with parallel processing.

## Learning goals

By the end of the activity, students will have practiced:

- Git and VS Code workflow
- Python virtual environments
- Installing packages with `pip`
- Downloading files with `yt-dlp`
- Reading CSV files with Python's built-in `csv` module
- Writing functions
- Measuring execution time
- Saving a simple Markdown report
- Using `multiprocessing.Pool`

## Phase handouts

Work through the phases in order:

1. [Phase 01: Preparation](phase-01.md)
2. [Phase 02: Build MVP](phase-02.md)
3. [Phase 03: Refactor to improve](phase-03.md)
4. [Phase 04: Read the data](phase-04.md)
5. [Phase 05: Download in serial](phase-05.md)
6. [Phase 06: Parallelize and compare](phase-06.md)
7. [Phase 07: Submit your work](phase-07.md)
8. [Phase 08: Add video metadata](phase-08.md)
9. [Phase 09: Make the downloader safer](phase-09.md)
10. [Phase 10: Request feedback](phase-10.md)

## Classroom rules

- Complete each in-class phase within the time limit shown in the phase title.
- If you finish early, do not start implementing the next phase. Wait for the instructor.
- Each table has 1 help request from another table.
- Each table has 1 help request from the Stelios team.
- If you fall behind, join the person next to you and continue from their current phase.

## Project structure

```text
bda-capstone-1/
├── README.md
├── phase-01.md
├── phase-02.md
├── phase-03.md
├── phase-04.md
├── phase-05.md
├── phase-06.md
├── phase-07.md
├── phase-08.md
├── phase-09.md
├── phase-10.md
├── requirements.txt
├── assets/
│   ├── add-collaborator-github.png
│   ├── assign-issue.png
│   └── create-issue.png
├── data/
│   └── video_urls.csv
└── reports/
    └── .gitkeep
```

Students will create these files and folders during the phases:

- `main.py`
- `library.py`
- `videos/`
- `data/video_metadata.csv`

## Important notes

- Download only videos that are appropriate for class use.
- Do not commit downloaded video files to Git.
- The `videos/` folder is for downloaded videos.
- The `reports/` folder is for the generated Markdown report.
- If `yt-dlp` stops working, update it:

```bash
pip install --upgrade yt-dlp
```

from library import *
import time
from multiprocessing import Pool
import threading
from concurrent.futures import ThreadPoolExecutor

if __name__ == "__main__":

    download_video("https://www.youtube.com/watch?v=jNQXAC9IVRw")

    url_list = read_video_urls("data/video_urls_updated.csv")

    serial_time = 0

    metadata_rows = []

    serial_results = []

    # Clear download_results.txt
    with open("reports/download_results.txt", "w", encoding="utf-8") as file:
        pass

    for i, url in enumerate(url_list):
        start = time.perf_counter()
        result = download_video(url)
        serial_results.append(result)
        end = time.perf_counter()
        try: 
            metadata = get_video_metadata(url)
            metadata_rows.append(metadata)
        except Exception as error:
            print(f"Problem obtaining video metadata: {error}.")
        elapsed = end - start
        serial_time += elapsed
        print(f"\nTime to download video {i + 1} was {round(elapsed, 2)} seconds.\n")
    
    print(f"Serial execution: {round(serial_time, 2)}")

    with open("reports/sequential_report.md", "w", encoding="utf-8") as file:
        file.write(f"""# Report

## Serial execution

Total time: {round(serial_time, 2)} seconds

Time complexity: n (amount of urls to process) x m (average size of video files)

Space complexity: n + m
"""
         )
        
#     # Previous method:
#     # with Pool(processes=5) as pool:
    with ThreadPoolExecutor() as executor:
        start = time.perf_counter()
        parallel_results = executor.map(download_video, url_list)
        end = time.perf_counter()
        elapsed = end - start
        parallel_time = round(elapsed, 2)
    
    print(f"Parallel execution: {parallel_time}")

    time_saved = serial_time - parallel_time
    percent_improvement = round(time_saved / serial_time * 100)

    with result_file_guard:
        with open("reports/sequential_report.md", "a", encoding="utf-8") as file:
            file.write(f"""   
## Parallel execution

Total time: {parallel_time} seconds

Speed improvement: {percent_improvement}%

## Download status:

"""
            )

            for result in parallel_results:
                if result["status"] == "failed":
                    file.write(f"\nFailed: {result['url']}")
                    file.write(f"\nError: {result['error']}")

    fieldnames = []
    if metadata_rows:
        for column, value in metadata.items():
            fieldnames.append(column)

    with open("data/video_metadata.csv", "w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames)
        writer.writeheader()
        writer.writerows(metadata_rows)
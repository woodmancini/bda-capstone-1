from library import download_video
from library import read_video_urls
import time
from multiprocessing import Pool

if __name__ == "__main__":

    download_video("https://www.youtube.com/watch?v=jNQXAC9IVRw")

    url_list = read_video_urls("data/video_urls.csv")

    serial_time = 0
    for i, url in enumerate(url_list):
        start = time.perf_counter()
        download_video(url)
        end = time.perf_counter()
        elapsed = end - start
        serial_time += elapsed
        print(f"\nTime to download video {i + 1} was {round(elapsed, 2)} seconds.\n")
    
    print(f"Serial execution: {round(serial_time, 2)}")

    with open("reports\sequential_report.md", "w", encoding="utf-8") as file:
        file.write(f"""# Report

## Serial execution

Total time: {round(serial_time, 2)} seconds

Time complexity: n (amount of urls to process) x m (average size of video files)
Space complexity: n + m
"""
         )

    with Pool() as pool:
        start = time.perf_counter()
        results = pool.map(download_video, url_list)
        end = time.perf_counter()
        elapsed = end - start
        parallel_time = round(elapsed, 2)
    
    print(f"Parallel execution: {parallel_time}")

    time_saved = serial_time - parallel_time
    percent_improvement = round(time_saved / serial_time * 100)

    with open("reports\sequential_report.md", "a", encoding="utf-8") as file:
        file.write(f"""   
## Parallel execution

Total time: {parallel_time} seconds

Speed improvement: {percent_improvement}%"""
        )
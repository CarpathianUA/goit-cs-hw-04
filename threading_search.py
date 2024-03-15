import os
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from constants.files import FILES_DIR, CHUNK_SIZE
from constants.threads import THREADS_NUM_COEF
from utils.find_words import find_words_in_files_threads, chunk_files


def threading_search():
    directory_path = Path(FILES_DIR)
    if next(directory_path.iterdir(), None) is None:
        raise ValueError(
            f"Specified dir for search {directory_path.absolute()} is empty"
        )
    chunk_size = CHUNK_SIZE

    absolute_paths = [entry.absolute() for entry in directory_path.iterdir()]
    chunks = list(chunk_files(absolute_paths, chunk_size))

    with ThreadPoolExecutor(max_workers=os.cpu_count() * THREADS_NUM_COEF) as executor:
        # map each chunk of files to a separate thread
        result_futures = executor.map(find_words_in_files_threads, chunks)
        results = list(result_futures)

    # merge the results from each chunk
    final_results = defaultdict(set)
    for result in results:
        for word, files in result.items():
            final_results[word].update(files)

    return final_results


if __name__ == "__main__":
    threading_search()

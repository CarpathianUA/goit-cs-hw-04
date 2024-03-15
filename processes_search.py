import os
from multiprocessing import Pool, Manager
from pathlib import Path

from constants.files import FILES_DIR, CHUNK_SIZE
from utils.find_words import find_words_in_files_processes, chunk_files


def processes_search():
    directory_path = Path(FILES_DIR)
    if next(directory_path.iterdir(), None) is None:
        raise ValueError(
            f"Specified dir for search {directory_path.absolute()} is empty"
        )
    chunk_size = CHUNK_SIZE
    absolute_paths = [entry.absolute() for entry in directory_path.iterdir()]
    chunks = list(chunk_files(absolute_paths, chunk_size))

    # init Manager and create a shared dictionary
    with Manager() as manager:
        shared_dict = manager.dict()

        with Pool(processes=os.cpu_count()) as pool:
            # create a list of tasks with shared_dict
            tasks = [(chunk, shared_dict) for chunk in chunks]

            # use starmap to pass multiple arguments to the worker function
            pool.starmap(find_words_in_files_processes, tasks)

        final_results = dict(shared_dict)

    return final_results


if __name__ == "__main__":
    processes_search()

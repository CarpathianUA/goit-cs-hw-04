import logging
from collections import defaultdict

from constants.words import WORDS


def find_words_in_files_threads(files):
    """
    Finds words in the given files and returns a dictionary with the word as key and a set of files as value.

    Parameters:
    - files: a list of file paths to search for words

    Returns:
    - words: a dictionary with words as keys and sets of file paths as values
    """
    words = defaultdict(set)
    if not files:
        raise ValueError("Files list is empty")
    for file in files:
        with open(file, "r") as f:
            for line in f:
                for word in line.split():
                    if word.lower() in WORDS:
                        words[word.lower()].add(file.__str__())
    return words


def find_words_in_files_processes(chunk, shared_dict):
    """
    Find words in files and update a shared dictionary with the results.

    Parameters:
    - chunk: list of files to process
    - shared_dict: dictionary to store the results

    Returns:
    None
    """
    words = defaultdict(set)
    for file in chunk:
        with open(file, "r") as f:
            for line in f:
                for word in line.split():
                    if word.lower() in WORDS:
                        words[word.lower()].add(file.__str__())

    # update the shared dictionary with results from this chunk
    for word, files in words.items():
        if word in shared_dict:
            # combine with existing sets of files for this word
            shared_dict[word] = shared_dict[word].union(files)
        else:
            shared_dict[word] = files


def chunk_files(file_paths, chunk_size):
    """
    A function that chunks a list of file paths into smaller lists based on the given chunk size.

    Parameters:
    - file_paths (list): A list of file paths to be chunked.
    - chunk_size (int): The size of each chunk.

    Returns:
    - generator: Yields chunks of file paths based on the chunk size.
    """
    for i in range(0, len(file_paths), chunk_size):
        yield file_paths[i : i + chunk_size]  # noqa

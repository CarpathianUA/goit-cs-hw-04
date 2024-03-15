import time


def time_tracker(func):
    """
    A decorator function that tracks the time taken for the input function to execute.
    """

    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {round(end - start, 4)} seconds")
        return result

    return wrapper

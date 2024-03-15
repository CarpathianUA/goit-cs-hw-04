from icecream import ic

import processes_search as ps
import threading_search as ts
from utils.generate_text import seed_files
from utils.measurement import time_tracker
from utils.exceptions import exceptions_handler


@exceptions_handler
@time_tracker
def run_threads():
    return ic(ts.threading_search())


@exceptions_handler
@time_tracker
def run_processes():
    return ic(ps.processes_search())


if __name__ == "__main__":
    seed_files()
    run_threads()
    run_processes()

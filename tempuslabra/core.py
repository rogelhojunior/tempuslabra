import time
from datetime import timedelta

def timeit(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()

        elapsed_time = end_time - start_time
        formatted_time = format_time(elapsed_time)

        print(f"{func.__name__} took {formatted_time} to run.")
        return result

    return wrapper

def format_time(seconds):
    td = timedelta(seconds=seconds)
    hours, remainder = divmod(td.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    formatted_params = []
    if hours:
        formatted_params.append(f'{int(hours)} hours')

    if minutes:
        formatted_params.append(f'{int(minutes)} minutes')

    if seconds:
        formatted_params.append(f'{int(seconds)} seconds')

    if milliseconds := td.microseconds // 1000:
        formatted_params.append(f'{int(milliseconds)} milliseconds')

    formatted_time = ", ".join(formatted_params)

    if ',' in formatted_time:
        formatted_time = ' and'.join(formatted_time.rsplit(',', 1))

    return formatted_time

import time
from datetime import timedelta
from .utils import i18n

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
    milliseconds = td.microseconds // 1000

    formatted_params = [
        i18n.t('hours', count=hours),
        i18n.t('minutes', count=minutes),
        i18n.t('seconds', count=seconds),
        i18n.t('milliseconds', count=milliseconds),
    ]

    formatted_params = list(filter(None, formatted_params))

    formatted_time = ", ".join(formatted_params)

    if len(formatted_params) > 1:
        formatted_time = ' and'.join(formatted_time.rsplit(',', 1))

    return formatted_time

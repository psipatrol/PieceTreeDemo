import time


def debug(func):
    def wrapper(*args, **kwargs):
        start_time = time.time_ns()
        result = func(*args, **kwargs)
        end_time = time.time_ns()
        print(f"DEBUG: {func.__name__} executed in {end_time - start_time} ns")
        return result
    return wrapper
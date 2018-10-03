import time
import functools
from copy import deepcopy
global_dict = {}


def cache(long_running_func):
    @functools.wraps(long_running_func)
    def inner(*args, **kwargs):
        key = args + tuple(kwargs.keys()) + tuple(kwargs.values())

        existent_value = global_dict.get(key)
        if existent_value:
            print(f"Woah I found out that {existent_value} already exists")
            copied_value = deepcopy(existent_value)
            return copied_value

        value = long_running_func(*args, **kwargs)
        copied_value = deepcopy(value)
        global_dict[key] = copied_value
        return value
    return inner


@cache
def params_count(*args, **kwargs):
    time.sleep(10)
    return list((1, 2, 3) + args + tuple(kwargs.values()))

"""
Функция для расчёта времени операции
"""
import time
from typing import Callable


def timer(func: Callable) -> Callable:
    def wrapped_func(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        func_time = round(time.time() - start, 2)
        print(f"Время выполнения операции: {func_time} c")
        return func

    return wrapped_func

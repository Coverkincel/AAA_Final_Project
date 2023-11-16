# decorators.py
import time
import random
from functools import wraps


# Шаблон принимает случайно генерируемое время (от 1 до 5с)
def log(template: str):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            duration = round(end_time - start_time + random.randint(1, 5))
            print(template.format(duration))
            return result
        return wrapper
    return decorator

from throttled import Throttled, rate_limiter, exceptions
from functools import wraps
import time

throttler = Throttled(
    key="api_operations",
    quota=rate_limiter.per_min(6)
)

def rate_limit(cost = 1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = throttler.limit(cost=cost)
            if result.limited:
                raise exceptions.LimitedError(rate_limit_result=result)
            else:
                print(f"Executing {func.__name__} with cost {cost}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@rate_limit(cost = 2)
def read_data():
    pass

@rate_limit(cost = 6)
def write_data():
    pass

read_data()
time.sleep(22)
write_data()
            
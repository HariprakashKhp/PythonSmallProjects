from throttled import Throttled, rate_limiter, exceptions
from functools import wraps
from datetime import timedelta
import backoff

def multi_rate_limit(per_second=None, per_min = None, per_30min = None, cost = 1):
    throttlers = []

    if per_second is not None:
        throttlers.append(
            ("per_second", Throttled(key="per_second", quote=rate_limiter.per_sec(per_second)))
        )

    if per_min is not None:
        throttlers.append(
            ("per_min", Throttled(key="per_min", quota=rate_limiter.per_min(per_min)))
        )

    if per_30min is not None:
        throttlers.append(
            ("per_30min", Throttled(key="per_30min", quota=rate_limiter.per_duration(timedelta(minutes=30), limit=per_30min)))
        )

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for name, throttler in throttlers:
                result =throttler.limit()
                if result.limited:
                    retry_after = result.state.retry_after
                    raise exceptions.LimitedError(rate_limit_result=result)
            return func(*args,  **kwargs)
        return wrapper
    return decorator


@backoff.on_exception(
    backoff.expo,
    exceptions.LimitedError,
    max_tries=5,
    base = 2,
    factor=1,
    max_value=60
)
@multi_rate_limit(per_second=5, per_min= 100, per_30min=1000)
def fetch_data_from_api(endpoint):
    print(f"Making API call to {endpoint}")
    return {"status": "success", "data":"sample data"}

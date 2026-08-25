from throttled import Throttled, RateLimiterType, rate_limiter, exceptions
from functools import wraps

def fixed_window():
    # Fixed Window
    throttle = Throttled(
        using=RateLimiterType.FIXED_WINDOW.value,
        quota=rate_limiter.per_min(60)
    )

    # cost = 1 as default
    result = throttle.limit("api_key")

    result = throttle.limit("api_key", cost = 5)

    result = throttle.limit("api_key", cost=0.5, timeout=1.5)

    if not result.limited:
        pass
    else: 
        print(f"Rate limited. Try again in {result.state.retry_after} seconds")


# Apply rate limiting to a function (1 call per minute)
@Throttled(key="/ping", quota=rate_limiter.per_min(1))
def ping() -> str:
    print("ping")
    return "ping"


ping()  # Returns "ping"
try:
    ping()  # Raises LimitedError if rate limit exceeded
except exceptions.LimitedError as exc:
    print(exc)  
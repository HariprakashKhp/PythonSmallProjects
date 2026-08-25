from throttled import Throttled, RateLimiterType, rate_limiter

# Fixed Window
throttle = Throttled(
    using=RateLimiterType.FIXED_WINDOW.value,
    quota=rate_limiter.per_min(60)
)

result = throttle.limit("api_key")
if not result.limited:
    pass
else: 
    print(f"Rate limited. Try again in {result.state.retry_after} seconds")

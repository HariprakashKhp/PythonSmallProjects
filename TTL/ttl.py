from concurrent.futures import ThreadPoolExecutor, Future
from threading import Lock
from cachetools import cached, TTLCache

lock = Lock()

if __name__ == "__main__":

    @cached(cache=TTLCache(maxsize=10, ttl=60), lock=lock)
    def do_something(x: str):
        print(x)

    with ThreadPoolExecutor() as executor:
        first: Future = executor.submit(do_something, "AAA")
        second: Future = executor.submit(do_something, "AAA")

    first.result()
    second.result()
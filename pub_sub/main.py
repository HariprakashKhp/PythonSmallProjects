import asyncio
from collections import defaultdict
from typing import Callable, Dict, List, Any, Coroutine

class PubSub:
    def __init__(self):
        self.subscribers: Dict[str, List[Callable[[Any], Coroutine]]] = defaultdict(list)
        self.queues: Dict[str, asyncio.Queue] = defaultdict(asyncio.Queue)
        self.tasks: List[asyncio.Task] = []

    def subscribe(self, topic: str, handler: Callable[[Any], Coroutine]):
        self.subscribers[topic].append(handler)

    async def publish(self, topic:str, message:Any):
        await self.queues[topic].put(message)

    async def _dispatch(self, topic: str):
        while True:
            msg = await self.queues[topic].get()
            handlers = self.subscribers.get(topic, [])
            for handler in handlers:
                asyncio.create_task(handler(msg))

    async def start(self):
        for topic in self.subscribers:
            self.tasks.append(asyncio.create_task(self._dispatch(topic)))

    async def stop(self):
        for task in self.tasks:
            task.cancel()
        await asyncio.gather(*self.tasks, return_exceptions=True)
    

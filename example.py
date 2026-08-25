import asyncio
from main import PubSub

async def log_handler(msg):
    print(f"[log] {msg}")

async def email_handler(msg):
    print(f"[email] Sending: {msg}")

async def main():
    engine = PubSub()
    engine.subscribe("user.registered", log_handler)
    engine.subscribe("user.registered", email_handler)

    await engine.start()
    await engine.publish("user.registered", {"user_id": 42, "email": "hello@example.com"})

    await asyncio.sleep(1)
    await engine.stop()

asyncio.run(main())
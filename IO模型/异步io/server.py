import threading
import asyncio


@asyncio.coroutine
def hello():
    print('hello')
    yield from asyncio.sleep(1)


loop = asyncio.get_event_loop()

tasks = [hello(),hello()]

loop.run_until_complete(asyncio.wait(tasks))

loop.close()
# Hey Mat!
# example client from:
# http://websockets.readthedocs.io/en/stable/intro.html

#!/usr/bin/env python
# req: python > 3.5 and asyncio package

import asyncio
import websockets

async def hello():
    async with websockets.connect('ws://localhost:8765') as websocket:

        name = input("What's your name? ")
        await websocket.send(name)
        print("> {}".format(name))

        greeting = await websocket.recv()
        print("< {}".format(greeting))

asyncio.get_event_loop().run_until_complete(hello())


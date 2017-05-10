# Hey Mat!
# example client from:
# http://websockets.readthedocs.io/en/stable/intro.html

#!/usr/bin/env python
# req: python > 3.5 and asyncio package

import asyncio
import websockets

async def hello(websocket, path):
    name = await websocket.recv()
    print("< {}".format(name))

    greeting = "Hello {}!".format(name)
    await websocket.send(greeting)
    print("> {}".format(greeting))

start_server = websockets.serve(hello, 'localhost', 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()


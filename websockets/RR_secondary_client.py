# Hey Mat!
# Borrowing from the example
# http://websockets.readthedocs.io/en/stable/intro.html

#!/usr/bin/env python
# req: python > 3.5 and asyncio package

import asyncio
import websockets

# Function to connect to the websocket, and just print whatever it receives
async def hello():
    async with websockets.connect('ws://localhost:8765') as websocket:
        greeting = await websocket.recv()
        # Just print the entire received package?
        print(greeting)

asyncio.get_event_loop().run_until_complete(hello())

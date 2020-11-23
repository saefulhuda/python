#!/usr/bin/env python

# WS server that sends messages at random intervals

import asyncio
import datetime
import random
import websockets

async def time(websocket, path):
	count = 1
	while True:
		now = datetime.datetime.utcnow().isoformat() + "Z"
		data = 'OK ' + str(count)
		count += 1
		await websocket.send(data)
		await asyncio.sleep(random.random() * 3)

start_server = websockets.serve(time, "127.0.0.1", 5678)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
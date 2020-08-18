# -*- coding: utf-8 -*-
# @Time    : 2020/8/11 21:07
# @Author  : 饭盆里
# @File    : websockets_server.py
# @Software: PyCharm
# @desc    :
#!/usr/bin/env python

import asyncio
import websockets

async def echo(websocket, path):
    name = await websocket.recv()
    print(f'<{name}')
    gretting = f"hello, {name}"

    await websocket.send(gretting)
    print(f'>{gretting}')

    async for message in websocket:
        await websocket.send(message)

asyncio.get_event_loop().run_until_complete(websockets.serve(echo, 'localhost', 8765))
asyncio.get_event_loop().run_forever()
# -*- coding: utf-8 -*-
# @Time    : 2020/8/11 21:02
# @Author  : 饭盆里
# @File    : websockets_client.py
# @Software: PyCharm
# @desc    :

#!/usr/bin/env python

import asyncio
import websockets

async def hello(uri):

    async with websockets.connect(uri) as websocket:
        name = input("what's your name?")

        await websocket.send(name)
        print(f">{name}")

        greeting = await websocket.recv()
        print(f"<{greeting}")

asyncio.get_event_loop().run_until_complete(
    hello('ws://localhost:8766'))

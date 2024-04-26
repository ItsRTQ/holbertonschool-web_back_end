#!/usr/bin/env python3
import asyncio
import random

async def async_generator():
    rand_list = []
    for i in range(10):
        random_num = random.randint(0, 10)
        await asyncio.sleep(1)
        rand_list.append(random_num)    
    return rand_list

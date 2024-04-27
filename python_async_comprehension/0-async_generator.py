#!/usr/bin/env python3
"""This module defines async_generator method"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[int, None]:
    """This method generates random numbers from 0 - 10"""

    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

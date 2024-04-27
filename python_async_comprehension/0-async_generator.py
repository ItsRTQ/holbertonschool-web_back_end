#!/usr/bin/env python3
"""This module defines async_generator method"""
import asyncio
import random


async def async_generator():
    """This method generates random numbers from 0 - 10"""

    for _ in range(10):

        await asyncio.sleep(1)
        yield random.randint(0, 10)

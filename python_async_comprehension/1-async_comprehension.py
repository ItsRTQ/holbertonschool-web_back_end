#!/usr/bin/env python3
"""This module defines async_comprehension method"""
import asyncio

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """This method collects 10 random numbers and return them"""

    result = []
    async for i in async_generator():
        result.append(i)
    return result

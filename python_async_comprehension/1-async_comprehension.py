#!/usr/bin/env python3
"""This module defines async_comprehension method"""
import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """This method collects 10 random numbers and return them"""

    return [num async for num in async_generator()]

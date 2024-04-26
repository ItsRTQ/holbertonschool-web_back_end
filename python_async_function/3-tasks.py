#!/usr/bin/env python3
"""This module defines the method task_wait_random"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Returns asyncio.Task method"""

    return asyncio.create_task(wait_random(max_delay))

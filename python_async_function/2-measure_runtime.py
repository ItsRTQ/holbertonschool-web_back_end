#!/usr/bin/env python3
"""This module defines measure_time method"""
import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
        Measures the execution time for wait_n(), and returns the wait_time
    """

    start = time.time()

    asyncio.run(wait_n(n, max_delay))

    end = time.time()
    total_time = end - start
    return float(total_time / n)

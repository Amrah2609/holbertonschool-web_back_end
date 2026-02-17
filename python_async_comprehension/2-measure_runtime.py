#!/usr/bin/env python3
"""
Docstring for python_async_comprehension.2-measure_runtime
"""

import asyncio
import time
asyncio_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measure the total runtime of async_comprehension
    """
    start_time = time.time()

    await asyncio.gather(*[asyncio_comprehension() for _ in range(4)])

    end_time = time.time()
    return end_time - start_time

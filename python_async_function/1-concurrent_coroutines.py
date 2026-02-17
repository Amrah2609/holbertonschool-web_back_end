#!/usr/bin/env python3
"""
Docstring for python_async_function.1-concurrent_coroutines
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Waits for n random delays between 0 and max_delay seconds
    and returns the list of delays.
    """

    delays = []
    task = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    for t in asyncio.as_completed(task):
        delays.append(await t)
    return delays

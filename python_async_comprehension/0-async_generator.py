#!/usr/bin/env python3
"""
Docstring for python_async_comprehension.0-async_generator
"""


import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Loop 10 times, each time asynchronously wait a
    random delay between 0 and 10 seconds,
    then yield the delay.
    """

    for i in range(10):
        await asyncio.sleep(1)
        i = random.uniform(0, 10)
        yield i

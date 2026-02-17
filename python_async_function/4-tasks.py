#!/usr/bin/env python3
"""
Docstring for python_async_function.4-tasks
"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Returns the list of all the delays (float values) of the tasks
    """

    delays = [await task_wait_random(max_delay) for i in range(n)]
    return sorted(delays)

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

    tasks = [task_wait_random(max_delay) for i in range(n)]
    delays = [await task for task in asyncio.as_completed(tasks)]
    return delays

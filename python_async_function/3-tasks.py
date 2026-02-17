#!/usr/bin/env python3
"""
Docstring for python_async_function.3-tasks
"""

import asyncio
wait = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Returns an asyncio.Task
    """
    return asyncio.create_task(wait(max_delay))

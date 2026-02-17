#!/usr/bin/env python3
"""
Docstring for python_async_comprehension.1-async_comprehension
"""

from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Returns the 10 random numbers from async_generator
    """
    return [i async for i in async_generator()]

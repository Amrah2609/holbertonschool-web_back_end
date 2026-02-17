#!/usr/bin/env python3
"""
Docstring for python_async_function.2-measure_runtime
"""

import time
import asyncio


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay)
    Args:
        n: The number of times to call wait_n
        max_delay: The maximum delay for each call to wait_n
    Returns:
        The total execution time in seconds
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time/n

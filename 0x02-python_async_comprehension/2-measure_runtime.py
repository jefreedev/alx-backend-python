#!/usr/bin/env python3
"""
Module for run time for four parallel comprehensions.
"""
import asyncio
import time
async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """Coroutine that executes async_comprehension 4 times
    using asyncio.gather measuring the total runtime and return it.
    """
    start = time.perf_counter()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    return time.perf_counter() - start

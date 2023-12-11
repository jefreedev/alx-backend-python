#!/usr/bin/env python3
"""Module
"""
from typing import List
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> list[float]:
    """Async routine that takes in two int args
    and returns a list of all the delays(float values)
    """
    tmp = [wait_random(max_delay) for _ in range(n)]
    tmp = asyncio.as_completed(tmp)
    delays = [await i for i in tmp]
    return delays

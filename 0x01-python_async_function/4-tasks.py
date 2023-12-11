#!/usr/bin/env python3
"""Tasks module
"""
from typing import List
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Another task with dif return val
    """
    tmp = [task_wait_random(max_delay) for _ in range(n)]
    tmp = asyncio.as_completed(tmp)
    delays = [await i for i in tmp]
    return delays

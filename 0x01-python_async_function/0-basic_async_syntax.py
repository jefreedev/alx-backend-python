#!/usr/bin/env python3
""" Module
"""
import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    """Async coroutine that takes in an int arg that awaits
    for random delay between 0 and max_delay seconds and 
    eventually returns it
    """
    random_num = random.uniform(0, max_delay)
    await asyncio.sleep(random_num)
    return random_num

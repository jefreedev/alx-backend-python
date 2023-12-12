#!/usr/bin/env python3
"""
Async Comprehensions Module
"""
from typing import List
async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """Coroutine that takes no arguments. Collects 10 random numbers
    using async comprehensing over async_generator then
    returns 10 random numbers
    """
    return [_ async for _ in async_generator()]

#!/usr/bin/env python3
"""Script to create class and store data"""

import redis
import uuid
from typing import Union, Callable, Any
import functools

class Cache:
    """Define Cache class for storing and retrieving data"""
    def __init__(self) -> None:
        """Initialize Redis instance and flush database"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @classmethod
    def count_calls(cls, method: Callable) -> Callable:
        """Decorator to count the number of calls to a method"""
        @functools.wraps(method)
        def wrapper(self, *args, **kwargs) -> Any:
            """Wrapper function to increment call count"""
            key = f"calls:{method.__qualname__}"
            self._redis.incr(key)
            return method(self, *args, **kwargs)
        return wrapper

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store data in Redis and return key"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(
            self, key: str, fn: Callable = None
            ) -> Union[str, bytes, int, float, None]:
        """Retrieve data from Redis using key"""
        value = self._redis.get(key)
        if value is None:
            return None
        if fn is not None:
            return fn(value)
        return value

    def get_str(self, key: str) -> Union[str, None]:
        """Retrieve string data from Redis using key"""
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Union[int, None]:
        """Retrieve integer data from Redis using key"""
        return self.get(key, fn=lambda d: int(d))

#!/usr/bin/env python3
'''Script to create class and store data'''

import redis
import uuid
from typing import Union, Callable, Any
import functools

class Cache:
    '''define self and store method'''
    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()

    @staticmethod
    def count_calls(method: Callable) -> Callable:
        '''count calls decorator'''
        @functools.wraps(method)
        def wrapper(self, *args, **kwargs) -> Any:
            '''wrapper function'''
            key = f"calls:{method.__qualname__}"
            self._redis.incr(key)
            return method(self, *args, **kwargs)
        return wrapper

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''store data in redis'''
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(
            self, key: str, fn: Callable = None
            ) -> Union[str, bytes, int, float, None]:
        '''get data from redis'''
        value = self._redis.get(key)
        if value is None:
            return None
        if fn is not None:
            return fn(value)
        return value

    def get_str(self, key: str) -> Union[str, None]:
        '''get string data from redis'''
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Union[int, None]:
        '''get integer data from redis'''
        return self.get(key, fn=lambda d: int(d))

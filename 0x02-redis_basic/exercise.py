#!/usr/bin/env python3
'''Script to create class and store data'''

import redis
import uuid
from typing import Union, Callable, Any
import functools

class Cache:
    '''define self and store method'''
    def __init__(self) -> None:
        '''initialize redis and flush db'''
        self._redis = redis.Redis()
        self._redis.flushdb()

    @staticmethod
    def call_history(method: Callable) -> Callable:
        '''count calls decorator'''
        @functools.wraps(method)
        def wrapper(self, *args, **kwargs) -> Any:
            '''wrapper function'''
            input_key = f"{method.__qualname__}:inputs"
            output_key = f"{method.__qualname__}:outputs"

            # Store input arguments
            self._redis.rpush(input_key, str(args))

            # Execute the original method to get the output
            output = method(self, *args, **kwargs)

            # Store the output
            self._redis.rpush(output_key, output)

            return output

        return wrapper

    @call_history
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

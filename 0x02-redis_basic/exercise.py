#!/usr/bin/env python3
'''Script to create class and store data'''

import redis
import uuid
from typing import Union


class Cache:
    '''define self and store method'''
    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

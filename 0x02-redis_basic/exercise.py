#!/usr/bin/env python3
""" a module that performs basic functions on redis """
import uuid
import redis


class Cache():
    """ a class that uses redis opps """

    def __init__(self):
        """ intializing redis """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data) -> None:
        """ assignng key value pair """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

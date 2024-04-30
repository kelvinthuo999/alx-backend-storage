#!/usr/bin/env python3
'''Funct to insert into a doc'''

import pymongo


def insert_school(mongo_collection, **kwargs):
    '''Function to insert into a doc'''
    return mongo_collection.insert(kwargs)

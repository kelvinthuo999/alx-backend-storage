#!usr/bin/env python3
'''Function to update data'''

import pymongo


def update_topics(mongo_collection, name, topics):
    '''Function to update data'''
    query = {"name": name}
    new_data = {"$set": {"topics": topics}}

    return mongo_collection.update_many(query, new_data)

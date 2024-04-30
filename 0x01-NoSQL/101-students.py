#!/usr/bin/env python3
'''function to return and sort avg score'''

import pymongo


def top_students(mongo_collection):
    '''function to sort scores'''
    result = mongo_collection.aggregate([
        {"$group": {
            "name": "$name",
            "averageScore": {"$avg": "$topics.score"}
        }},
        {"$sort": {"averageScore": -1}}
    ])

    return result 

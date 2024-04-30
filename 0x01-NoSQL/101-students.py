#!/usr/bin/env python3
'''function to return and sort avg score'''

import pymongo


def top_students(mongo_collection):
    '''function to sort scores'''
    result = [
        {"$group": {
            "name": "$name",
            "averageScore": {"$avg": "$topics.score"}
        }},
        {"$sort": {"averageScore": -1}}
    ]

    return list(mongo_collection.aggregate(result))

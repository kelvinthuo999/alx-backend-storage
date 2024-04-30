#!/usr/bin/env python3
'''function to return a specific collection'''

import pymongo


def schools_by_topic(mongo_collection, topic):
    '''funct to return a specific collection'''
    schools = mongo_collection.find({ "topics": topic})
    return schools

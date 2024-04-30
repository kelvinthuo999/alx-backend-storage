#!/usr/bin/env python3
''' Funct to list all docs in a collection'''

import pymongo


def list_all(mongo_collection):
    '''Function to display all docs'''
    documents = []

    for doc in mongo_collection.find():
        documents.append(doc)

    return documents

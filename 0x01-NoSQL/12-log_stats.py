#!/usr/bin/env python3
'''function to look at logs in db'''

from pymongo import MongoClient


if __name__ == "__main__":
    '''function to display all the logs in db'''
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    # Count total logs
    n_logs = nginx_collection.count_documents({})
    print(f'{n_logs} logs')

    # Aggregate counts for each method
    pipeline = [
        {"$group": {"_id": "$method", "count": {"$sum": 1}}},
        {"$sort": {"_id": 1}}
    ]
    method_counts = list(nginx_collection.aggregate(pipeline))

    # Print method counts
    print('Methods:')
    for method_count in method_counts:
        method = method_count["_id"]
        count = method_count["count"]
        print(f'\tmethod {method}: {count}')

    # Count logs with method=GET and path=/status
    status_check = nginx_collection.count_documents({"method": "GET", "path": "/status"})
    print(f'{status_check} status check')

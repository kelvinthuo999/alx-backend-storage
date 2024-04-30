#!/usr/bin/env python3
'''function to look at nginx logs'''

from pymongo import MongoClient

def log_stats(mongo_collection):
    """
    Display stats about Nginx logs stored in MongoDB.

    Args:
    - mongo_collection: pymongo collection object
    """
    # Get total number of logs
    total_logs = mongo_collection.count_documents({})

    # Get number of logs for each method
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {method: mongo_collection.count_documents({"method": method}) for method in methods}

    # Get number of logs with method=GET and path=/status
    status_check_count = mongo_collection.count_documents({"method": "GET", "path": "/status"})

    # Display stats
    print(f"{total_logs} logs")
    print("Methods:")
    for method, count in method_counts.items():
        print(f"    method {method}: {count}")
    print(f"{status_check_count} status check")

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs_collection = client.logs.nginx

    log_stats(logs_collection)

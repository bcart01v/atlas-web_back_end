#!/usr/bin/env python3
""" Log stats.
"""


from pymongo import MongoClient

def log_stats():
    """
    Provides some stats about Nginx logs stored in MongoDB
    """

    client = MongoClient("mongodb://localhost:27017/")

    db = client['logs']
    collection = db['nginx']


    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")

    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    status_check = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check} status check")

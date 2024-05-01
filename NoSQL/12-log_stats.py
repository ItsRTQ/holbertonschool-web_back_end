#!/usr/bin/env python3
"""This module prints data from a mongoDB database"""
import pymongo


def get_nginx_logs_stats(mongo_uri):
    """This method display the data form a mongoDB datbase"""

    client = pymongo.MongoClient(mongo_uri)
    db = client['logs']
    collection = db['nginx']
    total_logs_count = collection.count_documents({})
    print(f"{total_logs_count} logs")
    http_methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {
        method: collection.count_documents({
            "method": method}) for method in http_methods}
    print("Methods:")
    for method in http_methods:
        print(f"\tmethod {method}: {method_counts[method]}")
    status_logs_count = collection.count_documents({
        "method": "GET", "path": "/status"})
    print(f"{status_logs_count} status check")
    client.close()


if __name__ == "__main__":
    mongo_uri = 'mongodb://localhost:27017'

    print("Stats:")
    get_nginx_logs_stats(mongo_uri)

#!/usr/bin/env python3
import pymongo

def get_nginx_logs_stats(mongo_uri):
    client = pymongo.MongoClient(mongo_uri)
    
    db = client['logs']
    collection = db['nginx']
    
    total_logs_count = collection.count_documents({})
    
    print(f"Total logs: {total_logs_count} logs")
    
    http_methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {method: collection.count_documents({"method": method}) for method in http_methods}
    
    print("Methods:")
    for method in http_methods:
        print(f"\t{method}: {method_counts[method]}")
    
    status_logs_count = collection.count_documents({"method": "GET", "path": "/status"})
    
    print(f"Logs with method=GET and path=/status: {status_logs_count}")
    client.close()


if __name__ == "__main__":
    mongo_uri = 'mongodb://localhost:27017'
    get_nginx_logs_stats(mongo_uri)

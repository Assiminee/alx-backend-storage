#!/usr/bin/env python3
"""
Prints log information
"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx = client.logs.nginx

    print("{} logs".format(nginx.count_documents({})))

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = nginx.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, count))

    status_check_count = nginx.count_documents({"method":"GET", "path":"status"})
    print("{} status check".format(status_check_count))

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

    status_check_count = nginx.count_documents({"method":"GET", "path":"/status"})
    print("{} status check".format(status_check_count))

    print('IPs:')
    pipeline = [
        {'$group':
            {
                '_id': '$ip',
                'count': {'$sum': 1}
            }
        },
        {'$sort':
             {'count': -1}
         },
        {'$limit': 10}
    ]
    ip_count = nginx.aggregate(pipeline)

    for ip in ip_count:
        print("\t{}: {}".format(ip.get("_id"), ip.get("count")))
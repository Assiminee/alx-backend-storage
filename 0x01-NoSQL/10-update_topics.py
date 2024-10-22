#!/usr/bin/env python3
"""
Contains function update_topics
"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """
    changes all topics of a school document based on the name
    """
    doc = mongo_collection.find_one({"name": name})
    doc.update({"topics": topics})

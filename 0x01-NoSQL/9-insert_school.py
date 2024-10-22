#!/usr/bin/env python3
"""
Contains function insert_school
"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a collection based on kwargs
    """
    doc = mongo_collection.insert_one(kwargs)
    return doc.inserted_id

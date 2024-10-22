#!/usr/bin/env python3
"""
Contains function list_all
"""
import pymongo

def list_all(mongo_collection):
    """
    Finds all documents of a collection
    """
    return mongo_collection.find()

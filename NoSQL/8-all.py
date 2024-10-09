#!/usr/bin/env python3
""" list all documents in a collection.
"""


from pymongo import MongoClient


def list_all(mongo_collection):
    """ lists all documents in a collection
    """
    return list(mongo_collection.find())

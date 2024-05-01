#!/usr/bin/env python3
"""This modules defines list_all"""
import pymongo


def list_all(mongo_collection):
    """This method takes a mongo collection and returns a all documents"""

    data = mongo_collection.find()
    if data.count() == 0:
        return []
    else:
        return data

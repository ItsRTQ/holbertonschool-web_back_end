#!/usr/bin/env python3
"""This module defines school_by_topic"""
import pymongo

def schools_by_topic(mongo_collection, topic):
    """This method returns the list of school having a specific topic"""

    data = mongo_collection.find(topic)
    if data.count() == 0:
        return []
    else:
        return data

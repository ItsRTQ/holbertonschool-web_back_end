#!/usr/bin/env python3
"""This module defines update_topics"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """This module updates mongo_collection based on name,topics"""

    filters = {'name': name}
    update = {'$set': {'topics': topics}}
    mongo_collection.update_many(filters, update, {"multi": "true"})

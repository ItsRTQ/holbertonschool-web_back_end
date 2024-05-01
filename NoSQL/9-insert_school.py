#!/usr/bin/env python3
"""This module defines insert_school"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """This module inserts documents from kwargs to collection"""

    target_id = mongo_collection.insert(kwargs)
    return target_id

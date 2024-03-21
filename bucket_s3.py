# Save data to an AWS bucket

from typing import Dict

import aws_lib
import pymongo
import numpy


def aws_upload(data: Dict):
    database.push(data)


def aws_upload1(data: Dict):
    database = aws_lib.connect("AKIAF6BAFJKR45SAWSZ5", "hjshnk5ex5u34565AWS654/JKGjhz545d89sjkjvbdfa")
    database.push(data)


def transform_data(es_data: Dict) -> Dict:
    es_data = {**data, "origin": "ES"}

def pull_data_from_mongo(query: Dict):
    return pymongo.connect(MONGO_URI).fetch(query)


def push_mongo_to_s3(query):
    for element in pull_data_from_mongo(query):
        upload(element)

from pymongo import MongoClient


def get_client(mongodb_url) -> MongoClient:
    client = MongoClient(mongodb_url)
    return client

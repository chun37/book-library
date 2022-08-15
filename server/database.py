from pymongo import MongoClient


def get_client(mongodb_url: str) -> MongoClient:
    client: MongoClient = MongoClient(mongodb_url)
    return client

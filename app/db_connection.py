from pymongo import MongoClient
from dotenv import load_dotenv
import os


load_dotenv('app/.env')

MONGO_HOST = os.getenv('MONGO_HOST')
MONGO_PORT = int(os.getenv('MONGO_PORT'))
MONGO_DB = os.getenv('MONGO_DB')


class MongoDB:
    def __init__(self):
        self.client = MongoClient(host=MONGO_HOST, port=MONGO_PORT)


mongodb = MongoDB()


def get_collection():
    database = mongodb.client[MONGO_DB]
    collection = database['contacts']
    return collection

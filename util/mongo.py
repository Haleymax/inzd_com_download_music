import pymongo

from config.read_config import read_config
from util.logger import logger


class MongoClient:
    def __init__(self, host, port, database):
        try:
            mongodb_url = f'mongodb://{host}:{port}/'
            self.client = pymongo.MongoClient(mongodb_url)
            self.db = self.client[database]
            logger.info("successfull connected to MongoDB")
        except Exception as e:
            logger.error(f"failed to establish connection with mongodb : {e}")

    def query_all_data(self, collection):
        collection = self.db[collection]
        result = list(collection.find())
        return result

    def insert_data(self, collection, data):
        if isinstance(data, list):
            collection.insert_many(data)
        else:
            collection.insert_one(data)

    def check_data_exists(self, collection, query):
        collection = self.db[collection]
        esisting = collection.find_one(query)
        if esisting is None:
            logger.info(f"data is not existing {query}")
            return False
        else:
            logger.info(f"data is exists {query}")
            return True

    def close(self):
        if self.client:
            self.client.close()
            logger.info("MongoDB connection closed")

host = read_config.get_host()
port = read_config.get_mongo_port
database = read_config.get_database()

my_mongo_client = MongoClient(host, port, database)
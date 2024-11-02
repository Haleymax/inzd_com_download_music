import pymongo

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

    def close(self):
        """
        Close the connection to the MongoDB server.
        """
        if self.client:
            self.client.close()
            logger.info("MongoDB connection closed")
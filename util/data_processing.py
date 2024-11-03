from config.read_config import read_config
from util.logger import logger
from util.mongo import my_mongo_client


class Information:
    def __init__(self, collection):
        self.data = None
        self.collection = None

    def insert_data_to_mongo(self, data):
        try:
            exists = my_mongo_client.check_data_exists(self.collection, data)
            if exists:
                logger.info(f"no need to insert data {data}")
            else:
                my_mongo_client.insert_data(data)
                logger.info(f"the data {data} has been inserted")
        except Exception as e:
            logger.error(e)


    def query_data_from_mongo(self):
        try:
            result = my_mongo_client.query_all_data(self.collection)
            logger.info(f"the data {result}")
            return result
        except Exception as e:
            logger.error(e)
            return None

collect = read_config.get_collection()

information = Information(collect)
import os

import yaml

from settings.all_path import config_path
from util.logger import logger

config_file = os.path.join(config_path, "config.yml")

def load_yaml(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = yaml.safe_load(file)
    return data

class ReadConfig:
    def __init__(self):
        self.data = load_yaml(config_file)

    def get_baseurl(self):
        logger.info("读取目标网站的url")
        config = self.data["spider"]
        return str(config['target_url'])

    def get_user_agent(self):
        logger.info("读取浏览器用户代理")
        config = self.data["spider"]
        return str(config['agent'])

    def get_host(self):
        logger.info("获取主机地址")
        config = self.data["database"]
        return str(config['host'])

    def get_mongo_port(self):
        logger.info("获取mongodb的端口")
        config = self.data["database"]
        return str(config['port'])

    def get_collection(self):
        logger.info("获取集合")
        config = self.data["database"]
        return str(config['collection'])

    def get_database(self):
        logger.info("获取数据库")
        config = self.data["database"]
        return str(config['mongo_database'])


read_config = ReadConfig()

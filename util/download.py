import os.path
import threading

import requests

from settings.all_path import data_path
from util.logger import logger


def download(url, name):
    respone = requests.get(url)
    if respone.status_code == 200:
        name.replace(' ', '')
        file_name = f"{name}.mp3"
        file_path = os.path.join(data_path, "mp3", file_name)
        try:
            with open(file_path, 'wb') as f:
                f.write(respone.content)
            logger.info(f"{name} ,下载成功")
        except Exception as e:
            logger.warning(f"write file faild because : {e}")
    else:
        logger.warning("fail link")


def start_download_thread(url, name):
    thread = threading.Thread(target=download, args=(url, name))
    thread.start()
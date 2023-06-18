# (c) @AbirHasan2005

import os
import logging

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)


class Config(object):
    API_ID = int(os.environ.get("API_ID", "4665778"))
    API_HASH = os.environ.get("API_HASH", "10e3ed833b0d09699973420d45359409")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6067088569:AAFuJk7fdGfDceeqSHNf964d30hKiwNstoI")
    DOWNLOAD_DIR = os.environ.get("DOWNLOAD_DIR", "./downloads")
    LOGGER = logging
    OWNER_ID = int(os.environ.get("OWNER_ID", 5531584953))
    PRO_USERS = list(set(int(x) for x in os.environ.get("PRO_USERS", "1943966786 5109494250").split()))
    PRO_USERS.append(OWNER_ID)
    MONGODB_URI = os.environ.get("MONGODB_URI", "mongodb+srv://starvaccine12:ndgdluGNEmOGPCKl@cluster0.5esahzs.mongodb.net/?retryWrites=true&w=majority")
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001616237532"))
    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", "False"))

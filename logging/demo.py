# coding: utf-8

import logging
from logging.config import fileConfig
fileConfig('logger_config.conf')

from log4mongo.handlers import MongoHandler

logger = logging.getLogger()
mon = MongoHandler(host='121.42.33.117', database_name='mongo_logs')
logger.addHandler(mon)

def main():
    # logger.debug('I am here!')
    logger.debug('I am here!')
    logger.error('I am here!')

if __name__ == '__main__':
    main()

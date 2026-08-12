#!/usr/bin/python3

import logging

logging.basicConfig(level=logging.INFO, format= "%(asctime)s | %(name)s | %(levelname)s | %(message)s")

logging.info("Application started")
logging.warning("Something unusual happened")
logging.error("Something failed")

logger = logging.getLogger(__name__)
user = input("Enter UserName:")
logger.info("User %s login", user)


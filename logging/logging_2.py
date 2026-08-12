#!/usr/bin/python3

import logging

logging.basicConfig(level=logging.DEBUG, format = "%(asctime)s -- %(name)s -- %(levelname)s -- %(message)s")


only_logger = logging.getLogger(__name__)



display_handler = logging.StreamHandler()
display_handler.setLevel(logging.INFO)

file_handler = logging.FileHandler("aegis.log")
file_handler.setLevel(logging.DEBUG)


only_logger.addHandler(file_handler)
only_logger.addHandler(display_handler)
only_logger.propagate = False


console_formatter = logging.Formatter("%(levelname)s -- %(message)s")

file_formatter = logging.Formatter(
    "%(asctime)s -- %(name)s -- %(levelname)s -- %(message)s"
)

display_handler.setFormatter(console_formatter)
file_handler.setFormatter(file_formatter)

only_logger.info("Application Started")
only_logger.debug("He\'d entered")

# utils/logger.py
import logging

logging.basicConfig(filename="bot_log.txt", level=logging.INFO)

def log_message(message):
    logging.info(message)

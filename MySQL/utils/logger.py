# File: utils/logger.py

import logging
import os

log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

logger = logging.getLogger("app")
logger.setLevel(logging.INFO)

csv_formatter = logging.Formatter('%(asctime)s,%(levelname)s,%(message)s')

csv_file_handler = logging.FileHandler(f"{log_dir}/app_log.csv", mode="a", encoding="utf-8")
csv_file_handler.setLevel(logging.INFO)
csv_file_handler.setFormatter(csv_formatter)

console_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(console_formatter)

if logger.hasHandlers():
    logger.handlers.clear()

logger.addHandler(csv_file_handler)
logger.addHandler(console_handler)

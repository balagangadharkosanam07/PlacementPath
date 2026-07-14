import logging
import os

LOG_DIRECTORY = "logs"

os.makedirs(LOG_DIRECTORY, exist_ok=True)

logger = logging.getLogger("PlacementPortal")

logger.setLevel(logging.INFO)

formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(message)s"
)

file_handler = logging.FileHandler(
    os.path.join(LOG_DIRECTORY, "application.log")
)
file_handler.setFormatter(formatter)

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

if not logger.handlers:
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
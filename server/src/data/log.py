import logging
from django.conf import settings
import os


def get_logger(name: str, filename: str) -> logging.Logger:
    logger = logging.getLogger(name)
    
    path = os.path.join(settings.LOGGING_PATH, filename)
    
    logger.addHandler(logging.FileHandler(path))
    logger.setLevel(logging.INFO)

    return logger
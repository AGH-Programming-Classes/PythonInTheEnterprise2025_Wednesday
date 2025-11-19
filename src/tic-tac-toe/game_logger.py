import logging
import time
from functools import wraps

logger = logging.getLogger(__name__)
logging.basicConfig(filename="game.log", level=logging.INFO)

def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        curr_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        logger.info(f"{curr_time}: {func.__name__} called")

        return func(*args, **kwargs)

    return wrapper
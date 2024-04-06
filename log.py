from loguru import logger
import functions

logger.remove()
logger.add(  # Add a new logger with the following settings
    "logs.log",  # The output file
    level="INFO",  # The minimum logging level
    format="{time} {level} {message}",  # Custom format
    backtrace=True,  # Include a stack trace on error
    rotation="1 MB",  # Rotate the log file when it reaches 10 MB
)


def log_start():
    logger.info("Program started successfully.")

def log_end():
    logger.info("Program ended successfully.")

def log_in():
    username = functions.curr_user.get_current_user()
    logger.info(f"User {username} authorized.")

def log_out():
    username = functions.curr_user.get_current_user()
    logger.info(f"User {username} authorized.")

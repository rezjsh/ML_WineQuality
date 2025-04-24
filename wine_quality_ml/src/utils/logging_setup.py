import logging
import os
import traceback
from logging.handlers import RotatingFileHandler
from datetime import datetime
from functools import wraps
from contextlib import contextmanager

def setup_logging(log_dir='logs', log_level=logging.INFO):
    """
    Set up logging configuration for the project.
    
    Args:
        log_dir (str): Directory to store log files
        log_level (int): Logging level (default: logging.INFO)
    
    Returns:
        logging.Logger: Configured logger instance
    """
    # Create logs directory if it doesn't exist
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    
    # Create a logger
    logger = logging.getLogger('wine_quality')
    logger.setLevel(log_level)
    
    # Create formatters
    console_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s')
    
    # Create console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(console_formatter)
    logger.addHandler(console_handler)
    
    # Create file handler with rotation
    current_time = datetime.now().strftime('%Y%m%d_%H%M%S')
    log_file = os.path.join(log_dir, f'wine_quality_{current_time}.log')
    file_handler = RotatingFileHandler(
        log_file,
        maxBytes=10*1024*1024,  # 10MB
        backupCount=5
    )
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)
    
    return logger

def log_exceptions(logger):
    """
    Decorator to log exceptions that occur in a function.
    
    Args:
        logger: Logger instance to use for logging
    
    Returns:
        function: Decorated function with exception logging
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                logger.error(f"Exception in {func.__name__}: {str(e)}")
                logger.error(f"Traceback: {traceback.format_exc()}")
                raise
        return wrapper
    return decorator

@contextmanager
def exception_logger(logger):
    """
    Context manager for logging exceptions in a block of code.
    
    Args:
        logger: Logger instance to use for logging
    
    Example:
        with exception_logger(logger):
            # code that might raise an exception
    """
    try:
        yield
    except Exception as e:
        logger.error(f"Exception occurred: {str(e)}")
        logger.error(f"Traceback: {traceback.format_exc()}")
        raise

# Create a default logger instance
logger = setup_logging()

# Export commonly used functions
debug = logger.debug
info = logger.info
warning = logger.warning
error = logger.error
critical = logger.critical 
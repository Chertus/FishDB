import logging
import time
from config import LOG_PATH, ERROR_LOG_PATH

# Set up logging
logging.basicConfig(filename=LOG_PATH, level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

error_logger = logging.getLogger('error_logger')
error_handler = logging.FileHandler(ERROR_LOG_PATH)
error_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
error_handler.setFormatter(error_formatter)
error_logger.addHandler(error_handler)
error_logger.setLevel(logging.ERROR)

def log_performance_metrics(start_time, end_time, pages_scraped, avg_response_time, failed_requests):
    logging.info(f"Scraping Started: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start_time))}")
    logging.info(f"Scraping Ended: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(end_time))}")
    logging.info(f"Total Runtime: {end_time - start_time} seconds")
    logging.info(f"Pages Scraped: {pages_scraped}")
    logging.info(f"Average Response Time: {avg_response_time} seconds")
    logging.info(f"Failed Requests: {failed_requests}")

def log_error(error_message, exception):
    error_logger.error(f"Error: {error_message}. Exception: {exception}")

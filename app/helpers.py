import logging

# logging setting
def set_logging():
    logging.basicConfig(
        level=logging.INFO,
        # defining the format of loggings
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
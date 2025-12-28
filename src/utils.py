import logging
import sys
import time

def setup_logging():
    log_format = "%(asctime)s - %(levelname)s - %(message)s"

    logging.basicConfig(
        format=log_format,
        level=logging.INFO,
        handlers=[
            logging.FileHandler("execution.log"),
            logging.StreamHandler(sys.stdout)
        ]
    )

    with open("execution.log", "a") as f:
        f.write("\n")
 
    logging.info(f"New execution in {time.localtime().tm_hour}:{time.localtime().tm_min}:{time.localtime().tm_sec}")

    return logging.getLogger("NotionBot")

logger = setup_logging()
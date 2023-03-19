import logging as lg
import os
from datetime import datetime

# log file name
LOG_FILE_NAME = f"{datetime.now().strftime('%m%d%Y__%H%M%S')}.log"

#Log file dir
LOG_FILE_DIR = os.path.join(os.getcwd())
print(LOG_FILE_DIR)

#Log file path
LOG_FILE_PATH = os.path.join(LOG_FILE_DIR,LOG_FILE_NAME)

lg.basicConfig(
    filename=LOG_FILE_PATH,
    format = "[%(asctime)s] % (lineno)d %(name)s - %(levelname)s- %(message)s",
    level= lg.INFO
)

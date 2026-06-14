from datetime import datetime
import logging
import os

LOG_FILE=F"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"

dir_name=os.path.join(os.getcwd(),'Logs')

os.makedirs(dir_name,exist_ok=True)

LOG_FILE_PATH= os.path.join(dir_name,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s %(lineno)d %(name)s - %(levelname)s - %(message)s]",
    level=logging.INFO
)

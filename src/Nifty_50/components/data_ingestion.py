import os
import sys
from dataclasses import dataclass
from src.Nifty_50.logger import logging
from src.Nifty_50.utils import read_sql_data
from src.Nifty_50.exception import CustomException
from sklearn.model_selection import train_test_split

@dataclass
class DataIngestionConfig:
    raw_data_path = os.path.join('artifacts','raw.csv')
    train_data_path = os.path.join('artifacts','train.csv')
    test_data_path = os.path.join('artifacts','test.csv')

class DataIngestion:
    def __init__(self):
        logging.info("Inside DataIngestion Class")
        self.data_ingestion_config=DataIngestionConfig()
    
    def inititate_data_ingestion(self):
       try:
           logging.info("Inititating Data ingestion process...")
           df= read_sql_data()
           os.makedirs(os.path.dirname(self.data_ingestion_config.raw_data_path),exist_ok=True)
           df=df.iloc[:,:-1]
           df.to_csv(self.data_ingestion_config.raw_data_path,index=False,header=True)
           logging.info("Raw file is created")
           training_data, test_data= train_test_split(df, test_size=0.2, random_state=42)
           training_data.to_csv(self.data_ingestion_config.train_data_path,index=False,header=True)
           logging.info("Train file is created")
           test_data.to_csv(self.data_ingestion_config.test_data_path,index=False,header=True)
           logging.info("Test file is created")
           
           logging.info("Inititating Data ingestion process is finished")
           logging.info("End process")
           
           return(
               self.data_ingestion_config.train_data_path,
               self.data_ingestion_config.test_data_path
           )
           
       except Exception as e:
           raise CustomException(e,sys)

DataIngestion().inititate_data_ingestion()
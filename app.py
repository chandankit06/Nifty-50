from src.Nifty_50.exception import CustomException
from src.Nifty_50.logger import logging
from src.Nifty_50.components.data_ingestion import DataIngestion
from src.Nifty_50.components.data_transformation import DataTransofrmation
import warnings
warnings.filterwarnings('ignore')


if __name__=='__main__':
    logging.info('App Processing')

    data_ingestion_obj= DataIngestion()
    train_path,test_path=data_ingestion_obj.inititate_data_ingestion()
    logging.info('Inititated Data ingestion process')
    
    data_transformation_obj=DataTransofrmation()
    data_transformation_obj.initiate_data_transformation(train_path,test_path)
    
    logging.info('Inititated Data transformation process')
    



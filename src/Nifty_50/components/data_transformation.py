
from src.Nifty_50.components.data_ingestion import DataIngestion
from src.Nifty_50.exception import CustomException
from src.Nifty_50.logger import logging
from src.Nifty_50.utils import save_object


import os
import sys
import numpy as np
import pandas as pd
from dataclasses import dataclass


#preprocessor packages

from sklearn.preprocessing import StandardScaler,OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline

@dataclass
class DataTransformationConfig:
    preprocessor_path = os.path.join('artifacts','preprocessor.pkl')

class DataTransofrmation:
    def __init__(self):
        self.data_transformation_config= DataTransformationConfig()
    


    def initiate_data_transformation(self, train_path,test_path):
        
        '''
            Creating preprocessor object and pipelines for model
            
            StandardScaler,OneHotEncoder
            ColumnTransformer,SimpleImputer
            Pipeline
        '''
        try:
            input_train_data= pd.read_csv(train_path)
            input_test_data= pd.read_csv(test_path)

            numerical_features=['Open', 'High', 'Low', 'Close', 'Volume']
            categorical_features=['Date', 'Ticker']

            categorical_pipeline=Pipeline(steps=[
                 ('SimpleImputer', SimpleImputer(strategy='most_frequent'),
                 ('OneHotEncoder',OneHotEncoder() ),
                 ("StandardScaler",StandardScaler(with_mean=False))
                 )
            ])
            logging.info('Categorical Pipeline created')
            numerical_pipeline=Pipeline(steps=[
                ('SimpleImputer', SimpleImputer(strategy='median')),
                ("StandardScaler",StandardScaler())
            ])
            logging.info('Numerical Pipeline created')

            preprocessor= ColumnTransformer(transformers=[
                ('numerical_features',numerical_features, numerical_pipeline),
                                         ('categorical_features',categorical_features,categorical_pipeline)
            ])

            logging.info('Preprocessor created')
            # os.makedirs(os.makedirs(os.path.dirname(self.data_transformation_config.preprocessor_path),exist_ok=True))
            save_object(self.data_transformation_config.preprocessor_path,preprocessor)
            return preprocessor
        
        except Exception as e:
            raise CustomException(e,sys)

DataTransofrmation().initiate_data_transformation("artifacts/train.csv","artifacts/test.csv")

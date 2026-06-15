import os
import sys
import pymysql
import warnings
import pandas as pd
from dotenv import load_dotenv
from src.Nifty_50.exception import CustomException

import pickle

warnings.filterwarnings('ignore')
load_dotenv()

host=os.getenv('host')
username=os.getenv('username')
password=os.getenv('password')
collection=os.getenv('collection')

def read_sql_data():

    mysql_connection= pymysql.connect(
        host=host,
        user=username,
        password=password,
        database=collection
    )
    df= pd.read_sql('select * from nifty500_5yr_data',mysql_connection)
    return df
read_sql_data()


def save_object(file_path,obj):
    try:
        with open(file_path,'wb') as fd:
            pickle.dump(obj,fd)
    except Exception as e:
        raise CustomException(e,sys)

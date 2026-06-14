import os
from pathlib import Path
import logging
project_name="Nifty_50"


file_list=[
    # f"{project_name}/logger.py",
   

    f"src/{project_name}/__init__.py",
    f"src/{project_name}/exception.py",
    f"src/{project_name}/logger.py",
    f"src/{project_name}/utils.py",
    
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_transformation.py",
    f"src/{project_name}/components/data_monitor.py",
    
    f"src/{project_name}/pipelines/__init__.py",
    f"src/{project_name}/pipelines/prediction_pipeline.py",
    f"src/{project_name}/pipelines/training_pipeline.py",
    
    "setup.py",
    "main.py",
    "app.py",
    "requirements.txt", 
    ".env"
]

logging.basicConfig(
    level=logging.INFO
)

for i in file_list:
    path= Path(i)
    dir_name , file_name= os.path.split(path)

  
    if dir_name !='' :
        os.makedirs(dir_name,exist_ok=True)
    if not os.path.exists(file_name) or os.path.getsize(file_name)==0:
        file_path = os.path.join(dir_name,file_name)
        with open(file_path,'w') as fd:
            pass
    else:
        logging.info(f'{file_name} already exists')
    
    
    


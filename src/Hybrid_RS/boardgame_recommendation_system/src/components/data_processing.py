import os
import pandas as pd 
import numpy as np 
import pickle

from pathlib import Path
from src import logger
from src.utils.common import get_size
from src.entity.config_entity import (DataProcessingConfig)


class DataProcessing:
    def __init__(self, config: DataProcessingConfig):
        self.config = config

    def read_file(self, path_file:Path) -> pd.DataFrame:
        """
            Target: 
                Read  data file with format csv

            With Args:
                path_file (Path): file path which to be needed to read
            
            Returns:
                DataFrame Type
        """
        try:
            data = pd.read_csv(path_file,low_memory= False)
            name_file = path_file.split("/")[-1].split(".")[0]
            if len(data) > 0:
                logger.info(f"Read Successfully with the file's name is {name_file}")
                return data
            else:
                logger.info("The currently loaded data is emptyed")
        except Exception as e:
            raise e
        


    def save_dataset_processing(self, data: pd.DataFrame, pickle_file_name: str):
        """
        Target: 
            Save some vital dataset after handling process.

        With Args:
            data (DataFrame): dataset regarding 

        """
        try:
            # path = self.config.root_dir + "/" + file_name + ".csv"
            path_pickle = self.config.pickle_dir + "/" + pickle_file_name + ".pkl"
            file_name = path_pickle.split('/')[-1]
            if os.path.exists(path_pickle):
                logger.info(f"File {file_name} exists. Deleting the old file....")
                os.remove(path_pickle)
            else:
                logger.info(f"Create successfully a new file with name: {file_name} ....")

            pickle.dump(data, open(path_pickle, "wb"))
            # bg_pivot.to_csv(path_pickle, index=True)
            # folder_file = path.split('/')[-2]
            pickle_folder_file = path_pickle.split('/')[-2]
            # logger.info(f"File {file_name} inserts successfully into {folder_file}.")
            logger.info(f"File {pickle_file_name} inserts successfully into {pickle_folder_file}.")


        except Exception as e:
            raise e
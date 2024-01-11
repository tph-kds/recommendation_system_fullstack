import os
import pandas as pd 
import numpy as np 
import pickle
import nltk


from pathlib import Path
from src import logger
from nltk.stem import PorterStemmer
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

    def file_ratings_aplly_stems(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        Target: 
            Adjust data file regarding boardgame information.

        With Args:
            data (DataFrame): dataset about boardgame information
        
        Returns:
            A cleaned datasets DataFrame
        """
        try:
            
            ### Handle string
            data["main_tags"] = data["main_tags"].apply(self.__stems)


            name_file = self.config.knowledge_data_cb_preparing_file.split("/")[-1]
            logger.info(f" Adjust file {name_file} successfully.")
            return data
        
        except Exception as e:
            raise e       


    def save_dataset_processing(self, data: pd.DataFrame, file_name: str):
        """
        Target: 
            Save some vital dataset after handling process.

        With Args:
            data (DataFrame): dataset regarding 

        """
        try:
            path = self.config.root_dir + "/" + file_name + ".csv"
            file_name = path.split('/')[-1]
            if os.path.exists(path):
                logger.info(f"File {file_name} exists. Deleting the old file....")
                os.remove(path)
            else:
                logger.info(f"Create successfully a new file with name: {file_name} ....")
            
            folder_file = path.split('/')[-2]
            data.to_csv(path, index= False)
            logger.info(f"File {file_name} inserts successfully into {folder_file}.")

        except Exception as e:
            raise e

    def __stems(self, text):
        ps = PorterStemmer()
        l = []
        for i in str(text).split():
            l.append(ps.stem(str(i)))

        return " ".join(l)
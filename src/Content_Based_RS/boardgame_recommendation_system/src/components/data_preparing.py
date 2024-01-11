import pandas as pd 
import numpy as np 
import os
import re 

from src import logger
from pathlib import Path
from collections import defaultdict
from src.utils.common import get_size
from src.entity.config_entity import (DataPreparingConfig)

class DataPreparing:
    def __init__(self, config: DataPreparingConfig):
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
        

    def file_ratings(self, data: pd.DataFrame, bg_df: pd.DataFrame) -> pd.DataFrame:
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
            data["comment"] = data["comment"].apply(lambda x:x.split())
            data["comment"] = data["comment"].apply(self.__remove_space)
            data["comment"] = data["comment"].apply(self.__filter_non_latin)
            data["comment"] = data["comment"].apply(self.__filter_number_appear)
            data["comment"] = data["comment"].apply(lambda x: " ".join(x))
            data["comment"] = data["comment"].apply(lambda x: x.lower())
            data = data.sort_values(by= "boardgame_id")

            ## Combine all of boardgame's information with the general boardgame_id (PLus string)
            concatenated_text = defaultdict(str)
            for bg_unique in data["boardgame_id"].unique():
                test_cm = data[data["boardgame_id"] == bg_unique]["comment"]
                test_l = len(test_cm)
                str_test = ""
                for i in range(test_l):
                    str_test += list(test_cm)[i] + " "
                concatenated_text[bg_unique] = str_test
                # print(bg_unique)

            ## Create a new dataframe  
            new_data = {'boardgame_id': list(concatenated_text.keys()), 'comment_tags': list(concatenated_text.values())}
            ratings_cf = pd.DataFrame(new_data)

            ratings_cf = ratings_cf.rename(columns={"id": "boardgame_id" , "text_concatenated" : "comment_tags"})

            # take boardgame_id name and merge data
            new_df_1 = ratings_cf.merge(data, on = "boardgame_id", how="inner")

            new_df_1 = new_df_1[["boardgame_id", "comment_tags", "boardgame_name"]]
            # drop the several same row
            new_df_1 = new_df_1.drop_duplicates()
            
            # Merge with boardgame data
            cb_df = bg_df.merge(new_df_1, on="boardgame_id", how="inner")

            ## Create "common knowledge"
            cb_df["main_tags"] = cb_df["tags"] + cb_df["comment_tags"]
            ratings_bg_cf = cb_df[["boardgame_id", "boardgame_name", "main_tags"]]


            name_file = self.config.ratings_data_file.split("/")[-1]
            logger.info(f" Adjust file {name_file} successfully.")
            return ratings_bg_cf
        
        except Exception as e:
            raise e
        
    def save_dataset_preparing(self, data: pd.DataFrame, file_name: str):
        """
        Target: 
            Save some vital dataset after preparing process.

        With Args:
            data (DataFrame): dataset regarding 

        """
        try:
            path = self.config.root_dir + "/" + file_name + ".csv"
            if os.path.exists(path):
                file_name = path.split('/')[-1]
                logger.info(f"File {file_name} exists. Deleting the old file....")
                os.remove(path)
            else:
                logger.info(f"Create successfully a new file with name: {file_name} ....")
                
            data.to_csv(path, index=False)
            folder_file = path.split('/')[-2]
            logger.info(f"File {file_name} inserts successfully into {folder_file}.")

        except Exception as e:
            raise e

    def __remove_space(self, word):
        l = []
        for i in word:
            l.append(i.replace(" ", "").replace("-", "").replace(".", ""))
        return l

    ## Delete some especial letter and don't the Latinh Word
    def __filter_non_latin(self, list_word):
        l = []
        for text in list_word:
            if text != "Missing":
                    # loại bỏ những kí tự có &#
                    text = re.sub(r'&#[0-9]+', '', text)
                    # Loại bỏ các kí tự không phải Latin
                    latin_only = re.sub(r'[^\x00-\x7F]+', ' ', text)
                    # Loại bỏ các kí tự đặc biệt như '#'
                    clean_text = re.sub(r'[^A-Za-z0-9\s]', '', latin_only)
                    l.append(clean_text)
        return l

    def __filter_number_appear(self, list_word):
        l = []
        for text in list_word:
                    # loại bỏ những kí tự có số > chuỗi 4 vd: từ 1000
                    text = re.sub(r'[0-9][0-9][0-9][0-9]+', '', text)
                    l.append(text)
        return l
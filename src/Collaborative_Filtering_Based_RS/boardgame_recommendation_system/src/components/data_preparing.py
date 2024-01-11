import pandas as pd 
import numpy as np 
import os

from src import logger
from pathlib import Path
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
    def file_bg(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        Target: 
            Adjust data file regarding boardgame information.

        With Args:
            data (DataFrame): dataset about boardgame information
        
        Returns:
            A cleaned datasets DataFrame
        """
        try:
            data = data[["id", "primary"]]
            data  = data.rename(columns={"id" : "boardgame_id", "primary" : "boardgame_name"})

            name_file = self.config.boardgame_data_file.split("/")[-1]
            logger.info(f" Adjust file {name_file} successfully.")
            return data
        except Exception as e:
            raise e

    def file_ratings(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        Target: 
            Adjust data file regarding boardgame information.

        With Args:
            data (DataFrame): dataset about boardgame information
        
        Returns:
            A cleaned datasets DataFrame
        """
        try:
            # Choose a lot of users interacts with some boardgame items which have count > 50
            user_count_rating = data["user_name"].value_counts()  > 50
            # Lấy những index - name user who have usually interact
            index_user = user_count_rating[user_count_rating].index
            ## Loc some index_user above.
            ratings = data[data["user_name"].isin(index_user)]
            ### Get some vital attribute
            ratings_bg = ratings[["user_name", "rating", "boardgame_id", "boardgame_name"]]
            # Tính số lượng ratings từ các user - Calculate ratings count from users which depended on boardgame_name
            number_of_ratings_bg = ratings_bg.groupby("boardgame_name")["rating"].count().reset_index()
            # Tính trung bình ratings từ các user - Calculate ratings mean from users which depended on boardgame_name 
            mean_of_ratings_bg = ratings_bg.groupby("boardgame_name")["rating"].mean().reset_index()
            # Merge two dataframe number_of_ratings_bg and mean_of_ratings_bg above into one unique dataframe
            mean_and_number_ratings = number_of_ratings_bg.merge(mean_of_ratings_bg, on= "boardgame_name")
            mean_and_number_ratings = mean_and_number_ratings.rename(columns={"rating_x" : "rating_count", "rating_y" : "rating_mean"})

            ### conbine count_rating with the original dataset
            ratings_bg_cf = ratings_bg.merge(mean_and_number_ratings, on = "boardgame_name")
            ## Refine the information for user's ratings count > 30
            ratings_bg_cf = ratings_bg_cf[ratings_bg_cf["rating_count"] > 30]


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

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
            colss = ['id', 'primary', 'image']
            bg_df = data[colss].rename(columns={"id" : "boardgame_id" , "primary" : "boardgame_name"})
            
            name_file = self.config.boardgame_data_file.split("/")[-1]
            logger.info(f" Adjust file {name_file} successfully.")
            return bg_df
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
            ## Calculate rating count of the boardgames
            test = data.groupby(["boardgame_id", "boardgame_name"])["rating"].count()
            df_test = pd.DataFrame(test)
            df_test = df_test.reset_index()
            df_test = df_test.rename(columns= {"rating" : "rating_counts"})
            
            ## Calculate rating mean of the boardgames
            test1 = data.groupby(["boardgame_id", "boardgame_name"])["rating"].mean()
            df_test_1 = pd.DataFrame(test1)
            df_test_1 = df_test_1.reset_index()
            df_test_1 = df_test_1.rename(columns= {"rating" : "rating_averages"})
            ## Merge two dataframe including df_test_1 : take rating mean of the boardgames, df_test : take rating count of the boardgames
            df_test_all = df_test.merge(df_test_1, on=["boardgame_id","boardgame_name"])
            ## Merge 2 original dataset
            main_df = df_test_all.merge(bg_df, on=["boardgame_id","boardgame_name"], how="left") # do image có một số boardgame không có ảnh nên nếu gộp lại thì nó bỏ đi các null, vì vậy how= "left để loại bỏ trường hợpp này"

            # Calculate all the components 
            number_of_ratings = main_df["rating_counts"]
            ratings = main_df["rating_averages"]
            ratings_average = main_df["rating_averages"].mean()
            minimum_list = main_df["rating_counts"].quantile(0.75)
            
            # Calculate all the components - create weight_ratings columns  
            main_df["weight_ratings"] = ((ratings*number_of_ratings) + (ratings_average * minimum_list)) / (number_of_ratings + minimum_list)
            # Arrange rows by "weight_ratings"
            main_df = main_df.sort_values(by= ["weight_ratings"], ascending=False)
            
            name_file = "weight_ratings"
            logger.info(f" Create file {name_file} successfully.")
            return main_df
        
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

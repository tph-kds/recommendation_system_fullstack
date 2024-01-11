import os
import pickle
import numpy as np 
import pandas as pd 

from src import logger
from pathlib import Path
from src.entity.config_entity import (ModelConfig)
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer



class Model:
    def __init__(self, config: ModelConfig):
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
            data = pd.read_csv(path_file,low_memory= False )
            name_file = path_file.split("/")[-1].split(".")[0]
            if len(data) > 0:
                logger.info(f"Read Successfully with the file's name is {name_file}")
                return data
            else:
                logger.info("The currently loaded data is emptyed")
        except Exception as e:
            raise e
        
    def calculate_similarity(self, vector: list) -> list:
        """
        Target: 
            calculate similarity depend on interaction between users with item - boardgame

        With Args:
            vector: list embedded information from dataset's common knowledge.
        
        Returns:
            A list
        """
        try:
            similarity = cosine_similarity(vector)

            logger.info(f" Calculate Similarity Values Successfully.")
            return similarity
        
        except Exception as e:
            raise e

    def embedding_vector(self, data: pd.DataFrame, max_features: int, stop_words : str):
        """
        Target: 
            Create vector depend on "main_tags" - knowledge for boardgame

        With Args:
            data (DataFrame): dataset about boardgame information
        
        """
        try:
            cv = CountVectorizer(max_features=max_features, stop_words=stop_words)
            vector = cv.fit_transform(data["main_tags"])

            name_file = self.config.knowledge_stems_cb.split("/")[-1]
            logger.info(f" Embedding vector successfully from file {name_file}.")
            return vector
        
        except Exception as e:
            raise e

    def save_dataset_model(self, data: pd.DataFrame, similarity : list, vector: list, file_name_pickle: list):
        """
        Target: 
            Save some vital dataset after handling process.

        With Args:
            data (DataFrame): dataset regarding 

        """
        try:
            # path = self.config.root_dir + "/" + file_name + ".csv"
            path_data = self.config.pickle_dir + "/" + file_name_pickle[0] + ".pkl"
            path_similarity = self.config.pickle_dir + "/" + file_name_pickle[1] + ".pkl"
            path_vector = self.config.pickle_dir + "/" + file_name_pickle[2] + ".pkl"
            path_pickle = [path_data, path_similarity, path_vector]
            for i in range(len(file_name_pickle)):
                file_name = path_pickle[i].split('/')[-1]
                if os.path.exists(path_pickle[i]):
                    logger.info(f"File {file_name} exists. Deleting the old file....")
                    os.remove(path_pickle[i])
                else:
                    logger.info(f"Create successfully a new file with name: {file_name} ....")

            pickle.dump(data, open(path_data, "wb"))
            pickle.dump(similarity, open(path_similarity, "wb"))
            pickle.dump(vector, open(path_vector, "wb"))
            for i in range(len(file_name_pickle)):
                pickle_folder_file = path_pickle[i].split('/')[-2]
                pickle_file_name = path_pickle[i].split('/')[-1]
                logger.info(f"File {pickle_file_name} inserts successfully into {pickle_folder_file}.")

        except Exception as e:
            raise e
        



    def recommendation_system_cb(self, data: pd.DataFrame, similary: list, boardgame:str, k:int):
        index  = data[data["boardgame_name"] == boardgame].index[0]
        distances = sorted(list(enumerate(similary[index])), reverse= True, key= lambda x : x[1])
        for distance in distances[1:k]:
            print(data.iloc[distance[0]]["boardgame_name"])
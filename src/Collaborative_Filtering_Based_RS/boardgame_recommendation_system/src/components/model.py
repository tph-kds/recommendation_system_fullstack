import os
import pickle
import numpy as np 
import pandas as pd 


from math import sqrt
from src import logger
from pathlib import Path
from sklearn.metrics import mean_squared_error
from sklearn.neighbors import NearestNeighbors
from src.entity.config_entity import (ModelConfig)


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
            ## Create Matrix for the User_Boardgame Interaction using pivot function
            bg_pivot = data.pivot_table(columns="user_name", index="boardgame_name", values="rating")
            # Fill all of Nan to 0
            bg_pivot.fillna(0, inplace = True)

            name_file = self.config.ratings_data_file.split("/")[-1]
            logger.info(f" Adjust file {name_file} successfully.")
            return bg_pivot
        
        except Exception as e:
            raise e
        
    def create_model(self,bg_pivot : pd.DataFrame, model_name: str, boardgame_name: str):
        """
        Target: 
            Create a model in order to predict and get some boardgame recommedation.

        With Args:
            data (DataFrame): dataset about boardgame information
        
        """
        try:
            # data.set_index("boardgame_name", inplace=True)
            boardgame_sparse = bg_pivot

            model = NearestNeighbors(metric="cosine", algorithm="brute")
            model.fit(boardgame_sparse)
            
            logger.info(f" Create a model successfully using NearestNeighbors.")

            model_path_pickle = self.config.pickle_dir + "/" + model_name + ".pkl"
            bg_name_path_pickle = self.config.pickle_dir + "/" + boardgame_name + ".pkl"
            model_name = model_path_pickle.split('/')[-1]
            bg_name = model_path_pickle.split('/')[-1]
            if os.path.exists(model_path_pickle):
                logger.info(f"File {model_name} exists. Deleting the old file....")
                os.remove(model_path_pickle)
            else:
                logger.info(f"Create successfully a new file with name: {model_name} ....")
            
            if os.path.exists(bg_name_path_pickle):
                logger.info(f"File {bg_name} exists. Deleting the old file....")
                os.remove(bg_name_path_pickle)
            else:
                logger.info(f"Create successfully a new file with name: {bg_name} ....")
            boardgame_name_all = bg_pivot.index

            pickle.dump(model, open(model_path_pickle, "wb"))
            pickle.dump(boardgame_name_all, open(bg_name_path_pickle, "wb"))
            
            folder_model = model_path_pickle.split('/')[-2]
            folder_bgname = model_path_pickle.split('/')[-2]
            logger.info(f"File {model_name} inserts successfully into {folder_model}.")
            logger.info(f"File {bg_name} inserts successfully into {folder_bgname}.")
        
        except Exception as e:
            raise e



    def collaborative_filtering_RS_ver1(self, model, boardgame_name, bg_pivot, k):
        boardgame_idx = np.where(bg_pivot.index == boardgame_name)[0][0]
        distance, boardgame_idx_corr = model.kneighbors(bg_pivot.iloc[boardgame_idx, :].values.reshape(1,-1), n_neighbors=k)
        for i in range(len(boardgame_idx_corr)):
            boardgames = bg_pivot.index[boardgame_idx_corr[i]]
            for bg_name in boardgames:
                print(bg_name)

    def collaborative_filtering_RS_ver2(self, model, boardgame_name, bg_pivot, k):
        boardgame_idx = np.where(bg_pivot.index == boardgame_name)[0][0]
        distance, boardgame_idx_corr = model.kneighbors(bg_pivot.iloc[boardgame_idx, :].values.reshape(1,-1), n_neighbors=k)
        ## Item-based Recommendation Systems

        col_names = bg_pivot.index[boardgame_idx_corr[0]].tolist()
        zipped = list(zip(col_names[1:], distance[1:])) # bỏ chính nó
        sort = sorted(zipped, key=lambda x : x[1])
        # items_dict[boardgame_name] = sort
        for i in range(len(sort)):
            print(sort[i][0])
        # print(boardgame_idx_corr)
        # return sort

    def prediction_and_groundtruth(self,model,  bg_pivot: pd.DataFrame, k) -> pd.DataFrame:
        """
            Target: 
                Read  data file with format csv

            With Args:
                path_file (Path): file path which to be needed to read
            
            Returns:
                DataFrame Type
        """
        try:
            distance, boardgame_idx_corr = model.kneighbors(bg_pivot.values, n_neighbors=k)
            item_distances = 1 - distance 
            predictions = item_distances.T.dot(bg_pivot.values) / np.array([np.abs(item_distances.T).sum(axis = 1)]).T
            ground_truth = bg_pivot.values[item_distances.argsort()[0]]
            logger.info("Prediction and Create ground_truth successfully.")
            return predictions, ground_truth
        except Exception as e:
            raise e    

    def __rmse(self, predictions, ground_truth):
        predictions = predictions[ground_truth.nonzero()].flatten()
        ground_truth = ground_truth[ground_truth.nonzero()].flatten()
        return sqrt(mean_squared_error(predictions, ground_truth))

    def model_performance(self, predictions: list, ground_truth: list):
        """
        Target: 
            Save some vital dataset after handling process.

        With Args:
            data (DataFrame): dataset regarding 

        """
        try:
            error_rate = self.__rmse(predictions, ground_truth)
            accuracy = 100 - error_rate
            print(f"Accuracy of Model: {accuracy:.3f} %")
            print(f"RMSE: {error_rate:.3f} ")

        except Exception as e:
            raise e
import os
import pandas as pd 
import numpy as np 
import pickle

from pathlib import Path
from math import sqrt
from src import logger
from sklearn.metrics import mean_squared_error
from src.entity.config_entity import (EvaluateModelConfig)


class EvaluateModel:
    def __init__(self, config: EvaluateModelConfig):
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


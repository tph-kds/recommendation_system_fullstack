import os
import pickle
import numpy as np 
import pandas as pd 

from src import logger
from pathlib import Path
from sklearn.preprocessing import MinMaxScaler
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
        
        
    def read_pickle(self,path_pickle_data: Path, path_pickle_needed: Path):
        """
        Target: 
            Take two file contain the vital information for using to predict the result.

        With Args:
            path_pickle_data (Path): link file the first pickle arcording the data. 
            path_pickle_needed (Path): link file the another pickle arcording the reference info. 
        
        """
        try:
            with open(path_pickle_data, "rb") as f :
                data = pickle.load(f)
            with open(path_pickle_needed, "rb") as f :
                needed = pickle.load(f)
            
            data_name = path_pickle_data.split('/')[-1]
            needed_name = path_pickle_needed.split('/')[-1]
            logger.info(f"Read successfully file with name: {data_name} from source: {path_pickle_data}.")
            logger.info(f"Read successfully file with name: {needed_name} from source: {path_pickle_needed}.")

            return data, needed
        except Exception as e:
            raise e

    def predict_using_cb(self,data: pd.DataFrame, similarity: list, boardgame: str, k: int) -> pd.DataFrame :
        """
        Target: 
            Create a dataframe contain a list of predicted boardgames.

        With Args:
            data (pd.DataFrame) : data of the content based method
            similarity (list): similarity value.
            boardgame (str): boardgame name which needed to be predicted.
            k (int) : list count of the conference boargames.
        """
        try:
            boardgame_id_cb,boardgame_name_cb, similarity_k_cb = self.recommendation_system_cb(data, similary=similarity, boardgame=boardgame, k=k)
            similarity_dict_cb = {"boardgame_id": boardgame_id_cb,"boardgame_name" :boardgame_name_cb, "similarity_cb" : similarity_k_cb}
            similarity_df_cb = pd.DataFrame(similarity_dict_cb)
            
            logger.info(f"Predict successfully with Content_Based Recommendation System Method.")
            logger.info(f"Created and add successfully a Boardgame dataframe are predicted.")
            
            return similarity_df_cb
        except Exception as e:
            raise e

    def predict_using_cfb(self,model, bg_pivot, boardgame: str, k: int) -> pd.DataFrame :
        """
        Target: 
            Create a dataframe contain a list of predicted boardgames.

        With Args:
            model : model of the collaborative filtering based method
            bg_pivot : a dataframe .
            boardgame (str): boardgame name which needed to be predicted.
            k (int) : list count of the conference boargames.
        """
        try:
            boardgame_name_cfb, similarity_k_cfb = self.collaborative_filtering_RS(model, boardgame, bg_pivot, k)
            similarity_dict_cfb = {"boardgame_name" :boardgame_name_cfb, "similarity_cfb" : similarity_k_cfb}
            similarity_df_cfb = pd.DataFrame(similarity_dict_cfb)

            logger.info(f"Predict successfully with Collaborative_Filtering_Based Recommendation System Method.")
            logger.info(f"Created and add successfully a Boardgame dataframe are predicted.")
            
            return similarity_df_cfb
        except Exception as e:
            raise e
        
    def merge_data(self,similarity_df_cb: pd.DataFrame, similarity_df_cfb: pd.DataFrame, bg_info: pd.DataFrame) -> pd.DataFrame :
        """
        Target: 
            Create a new dataframe which have together boardgame_name.

        With Args:
            similarity_df_cb (pd.DataFrame) : dataframe of content based method.
            similarity_df_cfb (pd.DataFrame) : dataframe of collaborative filtering based method.
        """
        try:
            similarity_hb = similarity_df_cb.merge(similarity_df_cfb, on="boardgame_name", how="outer")
            bg_info = bg_info[["id", "primary"]]
            bg_info  = bg_info.rename(columns={"id" : "boardgame_id", "primary" : "boardgame_name"})
            similarity_hb = similarity_hb.merge(bg_info, on=["boardgame_name", "boardgame_id"])
            similarity_hb = similarity_hb[["boardgame_id", "boardgame_name", "similarity_cb", "similarity_cfb"]]
            similarity_hb = similarity_hb.fillna(0.0)
            logger.info(f"Merge successfully .")
            return similarity_hb
        except Exception as e:
            raise e
        
    def hybrid_recommendation_system(self,data_weight: pd.DataFrame, similarity_hb: pd.DataFrame) -> pd.DataFrame :
        """
        Target: 
            Create a dataframe contain a list of predicted boardgames.

        With Args:
            data_weight (pd.DataFrame) : the original weight value of data depend on boardgame and ratings of users
            similarity_hb (pd.DataFrame) : the synthesize similarity of two methods. (CB, CFB)

        """
        try:
            data_weight = data_weight[['boardgame_id', 'boardgame_name', 'image', 'weight_ratings']]
            data_rs = similarity_hb.merge(data_weight , on = ["boardgame_id", "boardgame_name"])
            # print(data_rs)

            # Normalize data
            Scaling = MinMaxScaler()
            data_scaled_rs = Scaling.fit_transform(data_rs[["similarity_cb", "similarity_cfb", "weight_ratings"]])
            data_normalized_rs = pd.DataFrame(data_scaled_rs, columns=["similarity_cb", "similarity_cfb", "weight_ratings"])
            data_rs[["similarity_normalized_cb", "similarity_normalized_cfb", "weight_normalized_ratings"]] = data_normalized_rs
            ## Each Cotribute definely have the same position. ==> 1/3
            data_rs["score_total"] = data_rs["similarity_normalized_cb"] * 1/3 + data_rs["similarity_normalized_cfb"] * 1/3 + data_rs["weight_normalized_ratings"] * 1/3
            data_rs = data_rs.sort_values(by = "score_total", ascending= False)
            data_rs_final = data_rs[['boardgame_id', 'boardgame_name', 'image','score_total']]
            data_rs_final = pd.DataFrame(data_rs_final)
            logger.info(f"Predict successfully with Hybrid Based Recommedation System.")
            return data_rs_final
        except Exception as e:
            raise e    


    def collaborative_filtering_RS(self, model, boardgame_name, bg_pivot, k):
        bg_name_list = []
        bg_id_list = []
        distance_list = []
        boardgame_idx = np.where(bg_pivot.index == boardgame_name)[0][0]
        distances, boardgame_idx_corr = model.kneighbors(bg_pivot.iloc[boardgame_idx, :].values.reshape(1,-1), n_neighbors=k)
        for i in range(len(boardgame_idx_corr)):
            boardgames = bg_pivot.index[boardgame_idx_corr[i]]
            distances_1 = distances[i]
            for bg_name, distance in zip(boardgames[1:], distances_1[1:]):
                bg_name_list.append(bg_name)
                distance_list.append(distance)
        return bg_name_list, distance_list

    def recommendation_system_cb(self, data, similary, boardgame, k):
        bg_name_list = []
        bg_id_list = []
        distance_list = []
        index  = data[data["boardgame_name"] == boardgame].index[0]
        distances = sorted(list(enumerate(similary[index])), reverse= True, key= lambda x : x[1])
        for distance in distances[1:k]:
            # print(data.iloc[distance[0]]["boardgame_name"])
            bg_id_list.append(data.iloc[distance[0]]["boardgame_id"])
            bg_name_list.append(data.iloc[distance[0]]["boardgame_name"])
            distance_list.append(distance[1])
        return bg_id_list, bg_name_list, distance_list
    

import pandas as pd
import numpy as np
import pickle
import os

from sklearn.preprocessing import MinMaxScaler

class Model:
    def __init__(self, data_cb, data_weight, similarity_cb,model_cfb,  boardgame,bg_pivot_cfb, k):
        self.data_cb = data_cb
        self.data_weight = data_weight
        self.similarity_cb = similarity_cb
        self.model_cfb = model_cfb
        self.boardgame = boardgame
        self.bg_pivot_cfb = bg_pivot_cfb
        self.k = k
    def __collaborative_filtering_RS(self):
        bg_name_list = []
        bg_id_list = []
        distance_list = []
        boardgame_idx = np.where(self.bg_pivot_cfb.index == self.boardgame)[0][0]
        distances, boardgame_idx_corr = self.model_cfb.kneighbors(self.bg_pivot_cfb.iloc[boardgame_idx, :].values.reshape(1,-1), n_neighbors=self.k)
        for i in range(len(boardgame_idx_corr)):
            boardgames = self.bg_pivot_cfb.index[boardgame_idx_corr[i]]
            distances_1 = distances[i]
            zipped = list(zip(boardgames[1:], distances_1[1:]))
            sort = sorted(zipped, key=lambda x : x[1])
            for bg_name, distance in sort:
                bg_name_list.append(bg_name)
                distance_list.append(distance)
        return bg_name_list, distance_list
    def __recommendation_system_cb(self):
        bg_name_list = []
        bg_id_list = []
        distance_list = []
        index  = self.data_cb[self.data_cb["boardgame_name"] == self.boardgame].index[0]
        distances = sorted(list(enumerate(self.similarity_cb[index])), reverse= True, key= lambda x : x[1])
        for distance in distances[1:self.k]:
            # print(self.data_cb.iloc[distance[0]]["boardgame_name"])
            bg_id_list.append(self.data_cb.iloc[distance[0]]["boardgame_id"])
            bg_name_list.append(self.data_cb.iloc[distance[0]]["boardgame_name"])
            distance_list.append(distance[1])
        return bg_id_list, bg_name_list, distance_list
    
    def hybrid_rs(self):
        boardgame_id_cb,boardgame_name_cb, similarity_k_cb = self.__recommendation_system_cb()
        similarity_dict_cb = {"boardgame_id": boardgame_id_cb,"boardgame_name" :boardgame_name_cb, "similarity_cb" : similarity_k_cb}
        similarity_df_cb = pd.DataFrame(similarity_dict_cb)

        boardgame_name_cfb, similarity_k_cfb = self.__collaborative_filtering_RS()
        similarity_dict_cfb = {"boardgame_name" :boardgame_name_cfb, "similarity_cfb" : similarity_k_cfb}
        similarity_df_cfb = pd.DataFrame(similarity_dict_cfb)

        similarity_hb = similarity_df_cb.merge(similarity_df_cfb, on="boardgame_name")

        data_rs = similarity_hb.merge(self.data_weight , on = ["boardgame_id", "boardgame_name"])
        Scaling = MinMaxScaler()
        data_scaled_rs = Scaling.fit_transform(data_rs[["similarity_cb", "similarity_cfb", "weight_ratings"]])
        data_normalized_rs = pd.DataFrame(data_scaled_rs, columns=["similarity_cb", "similarity_cfb", "weight_ratings"])
        data_rs[["similarity_normalized_cb", "similarity_normalized_cfb", "weight_normalized_ratings"]] = data_normalized_rs
        data_rs["score_total"] = data_rs["similarity_normalized_cb"] * 1/3 + data_rs["similarity_normalized_cfb"] * 1/3 + data_rs["weight_normalized_ratings"] * 1/3
        data_rs = data_rs.sort_values(by = "score_total", ascending= False)
        data_rs_final = data_rs[['boardgame_id', 'boardgame_name', 'image','score_total']]
        return data_rs_final
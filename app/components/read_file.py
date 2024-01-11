
import pandas as pd 
import pickle

def file():
    data_weight = pd.read_csv("app/artifacts/weight_hybdrid_RS_dataset.csv")
    data_weight = data_weight[['boardgame_id', 'boardgame_name', 'image', 'weight_ratings']]

    with open("app/artifacts/data_boardgame_content_based.pkl", "rb") as f :
        data_cb = pickle.load(f)
    with open("app/artifacts/similarity_boardgame_content_based.pkl", "rb") as f :
        similarity_cb = pickle.load(f)

    with open("app/artifacts/model_collaborative_filtering_based_RS.pkl", "rb") as f :
        model_cfb = pickle.load(f)
    with open("app/artifacts/bg_pivot_collaborative_filtering_based_RS.pkl", "rb") as f :
        bg_pivot_cfb = pickle.load(f)
    
    return data_weight, data_cb, similarity_cb, model_cfb, bg_pivot_cfb

def read_file_csv():
    data = pd.read_csv("app/artifacts/data_web.csv")
    return data

data = read_file_csv()




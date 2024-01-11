import pickle
from src.config.configuaration import ConfiguarationManager
from src.components.model import Model
from src import logger

STAGE_NAME = "Model Stage"

class ModelPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfiguarationManager()
        model_config = config.get_model_config()
        model_parmas = config.get_model_params()
        model = Model(config=model_config)
        # Read pickle file
        data_cb, similarity_cb = model.read_pickle(model_config.data_cb, model_config.similarity_cb)
        model_cfb, bg_pivot_cfb = model.read_pickle(model_config.model_cfb, model_config.bg_pivot_cfb)
        # Read File
        bg_info = model.read_file(model.config.bg_info)
        data_weight = model.read_file(model_config.weight_ratings_hb_file)

        similarity_df_cb = model.predict_using_cb(data_cb, similarity_cb, model_parmas.BOARDGAME_NAME, model_parmas.K)
        similarity_df_cfb = model.predict_using_cfb(model_cfb, bg_pivot_cfb, model_parmas.BOARDGAME_NAME, model_parmas.K)
        similarity_hb = model.merge_data(similarity_df_cb, similarity_df_cfb, bg_info)
        # print(similarity_hb)

        data_rs_final = model.hybrid_recommendation_system(data_weight, similarity_hb)
        print(data_rs_final[["boardgame_id", "boardgame_name"]])

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>  {STAGE_NAME} started  <<<<<<<<<<")
        obj = ModelPipeline()
        obj.main()
        logger.info(f">>>>>>>>>  {STAGE_NAME} completed <<<<<<<<<<<\n\n +x==================x+")
    except Exception as e:
        logger.exception(e)
        raise e
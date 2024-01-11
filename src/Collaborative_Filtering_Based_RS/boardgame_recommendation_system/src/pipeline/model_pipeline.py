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
        model_params = config.get_model_params()
        model = Model(config=model_config)
        # Read File
        ratings_df = model.read_file(model_config.ratings_data_file)
        bg_pivot = model.file_ratings(ratings_df)

        model.create_model(bg_pivot, model_name = "model_cfb", boardgame_name = "bg_name_cfb")
        with open(model_config.pickle_dir + "/" + "model_cfb.pkl", "rb") as f:
            model_nn = pickle.load(f)
        k = model_params.K
        # boardgame_name = "Marvel Champions: The Card Game"
        boardgame_name  = model_params.BOARDGAME_NAME 
        model.collaborative_filtering_RS_ver1(model_nn, boardgame_name, bg_pivot, k)
        model.collaborative_filtering_RS_ver2(model_nn, boardgame_name, bg_pivot, k)

        predictions, ground_truth = model.prediction_and_groundtruth(model_nn, bg_pivot, k)
        model.model_performance(predictions, ground_truth)



if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>  {STAGE_NAME} started  <<<<<<<<<<")
        obj = ModelPipeline()
        obj.main()
        logger.info(f">>>>>>>>>  {STAGE_NAME} completed <<<<<<<<<<<\n\n +x==================x+")
    except Exception as e:
        logger.exception(e)
        raise e